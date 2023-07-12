import cv2
import numpy as np

poster = cv2.imread("poster.jpg")
print(poster.shape)

rocket = poster[130:380, 390: 510]

poster[150:400, 200:320] = rocket
cv2.putText(poster, "Cropped Image using NumPy", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
cv2.imshow("poster", poster)

cv2.imshow("rocket", rocket)
cv2.waitKey(0)

