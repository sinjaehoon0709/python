#-*- coding: utf-8 -*-
import pygame
import random
pygame.init() #초기화 (반드시 필요)

#화면크기 설정
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("코딩쌤 초미남")

#이미지 불러오기 (배경)
bg = pygame.image.load("SolarSim/src/face.jpg") # Relative Path

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인

while running: # 반복
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크크
        if event.type == pygame.QUIT: #창 닫는 이벤트트
            running = False
        #                        Red             Green                  Blue
        #screen.blit(bg, (0,0)) #blit = 배경 그리기
        #screen.fill((33, 33, 67)) #배경을 이미지가 아닌 색으로 지정정하기
        pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit()