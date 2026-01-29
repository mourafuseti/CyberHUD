import cv2
import sys
import os

print("[*] Diagnosticando módulos de Visão Computacional...")

# TENTATIVA DE IMPORTAÇÃO EM CASCATA (FALLBACK ESTRUTURADO)
try:
    # Tentativa 1: Estrutura Clássica
    from mediapipe.python.solutions import face_detection as mp_face
    from mediapipe.python.solutions import hands as mp_hands
    from mediapipe.python.solutions import drawing_utils as mp_draw
    print("[+] Estrutura detectada: mediapipe.python.solutions")
except ImportError:
    try:
        # Tentativa 2: Estrutura Direta
        from mediapipe.solutions import face_detection as mp_face
        from mediapipe.solutions import hands as mp_hands
        from mediapipe.solutions import drawing_utils as mp_draw
        print("[+] Estrutura detectada: mediapipe.solutions")
    except ImportError:
        try:
            # Tentativa 3: Via Objeto Principal
            import mediapipe as mp
            mp_face = mp.solutions.face_detection
            mp_hands = mp.solutions.hands
            mp_draw = mp.solutions.drawing_utils
            print("[+] Estrutura detectada: mp.solutions")
        except Exception as e:
            print(f"[-] Erro crítico de dependência: {e}")
            sys.exit(1)

# CONFIGURAÇÕES VISUAIS (ESTILO CYBERPUNK)
CYAN = (255, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)

def run_hud():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[-] Erro: Câmera não encontrada. Verifique as permissões do Docker/VM.")
        return

    # Inicializando os Detectores
    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detector, \
         mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hand_detector:

        print("[!] HUD ATIVO. Pressione 'q' para encerrar.")

        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            # Processamento de imagem
            frame = cv2.flip(frame, 1) # Espelhar para interação natural
            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 1. DETECÇÃO DE ROSTO
            face_results = face_detector.process(rgb_frame)
            if face_results.detections:
                for detection in face_results.detections:
                    bbox = detection.location_data.relative_bounding_box
                    x, y, fw, fh = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                    
                    # Desenhar Retângulo de Scanner
                    cv2.rectangle(frame, (x, y), (x + fw, y + fh), RED, 2)
                    
                    # Detalhes de HUD nos cantos (Mira)
                    d = 25
                    cv2.line(frame, (x, y), (x + d, y), WHITE, 3)
                    cv2.line(frame, (x, y), (x, y + d), WHITE, 3)
                    
                    cv2.putText(frame, "USER: LEONARDO FUSETI", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)

            # 2. DETECÇÃO DE MÃOS
            hand_results = hand_detector.process(rgb_frame)
            if hand_results.multi_hand_landmarks:
                for hand_lms in hand_results.multi_hand_landmarks:
                    # Desenha o esqueleto da mão
                    mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS,
                                         mp_draw.DrawingSpec(color=CYAN, thickness=2, circle_radius=2),
                                         mp_draw.DrawingSpec(color=WHITE, thickness=1))
                    
                    cv2.putText(frame, "BIOMETRIC SCAN: AUTHORIZED", (20, 40), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, CYAN, 2)

            # 3. OVERLAY ESTÁTICO
            cv2.putText(frame, "DEFESA CIBERNETICA - HUD V1.0", (w - 280, h - 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, WHITE, 1)

            cv2.imshow("Cyber HUD Project", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_hud()