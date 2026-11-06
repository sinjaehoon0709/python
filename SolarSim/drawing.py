#-*- coding: utf-8 -*-
import pygame

pygame.init() #초기화 (반드시 필요)

#화면크기 설정
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("1106")

r = 120

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인

while running: # 반복
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크크
        if event.type == pygame.QUIT: #창 닫는 이벤트트
            running = False

    #배경색 설정
    screen.fill((255,255,255))

    #직선 그리기
    #pygame.draw.line(1,2,3,4,5)
    pygame.draw.line(screen, (25, 225, 125), (0,0), (screen_width, screen_height), 30) # (대상,색상,시작점,끝점,긁기)
    pygame.draw.line(screen, (0, 225, 0), (0,screen_height), (screen_width, 0), 30)

    #선 여러개 긋기 (반복문 활용)
    for i in range(0,480,30): # 세로줄
        pygame.draw.line(screen, (0, 0, 225), (i, 0), (i, 640))
    for i in range(0, 640, 30): # 가로줄
        pygame.draw.line(screen, (0, 0, 225), (0, i), (480, i))

    #원 그리기
    pygame.draw.circle(screen, (0, 225, 100), (screen_width / 2, screen_height / 2), 100)#채워진 원 (대상,색상,중심점,반지름)
    pygame.draw.circle(screen, (225, 0, 0), (screen_width / 2, screen_height / 2), 200, 50)#테두리 원 (대상,색상,중심점,반지름,선굵기)

    #사각형
    pygame.draw.rect(screen, (55, 55, 225), (screen_width / 2, screen_height / 2, 100, 100))#채워진 사각형 (대상,색상,시작점 + 가로크기 + 세로크기)
    pygame.draw.rect(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, 100, 200), 5)#테두리 사각형 (대상,색상,시작점 + 가로크기 + 세로크기,선굵기)

    #타원
    pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 200))#채워진 타원 (대상,색상,시작점 + 가로크기 + 세로크기)
    pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2, screen_height / 2,200,100), 5)#테두리 타원 (대상,색상,시작점 + 가로크기 + 세로크기,선굵기)

    pygame.draw.ellipse(screen, (55, 55, 225), (screen_width / 2 - 100, screen_height / 2 - 100, 100, 100))#채워진 타원 (대상,색상,시작점 + 가로크기 + 세로크기)
    pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2 - 100, screen_height / 2 - 100, 1000, 100), 5)#테두리 타원 (대상,색상,시작점 + 가로크기 + 세로크기,선 굵기)

    # # 다각형
    pygame.draw.polygon(screen, (0, 0, 0), [[100,0],[0,200],[200,200]])#삼각형 / 점은 3개 이상. 윗쪽부터 반시계 방향으로 좌표 작성
    pygame.draw.polygon(screen, (0, 0, 0), [[100,0],[0,100],[0,200],[100,300],[200,200],[200,100]])#육각형. 점의 개수만큼 추가하면 됨.

    pygame.display.update()#실시간으로 업데이트
#종료처리
pygame.quit()