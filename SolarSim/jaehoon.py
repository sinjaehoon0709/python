#-*- coding: utf-8 -*-
import pygame

pygame.init() #초기화 (반드시 필요)

#화면크기 설정
screen_width = 1600
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("코딩쌤 초미남")

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인

while running: # 반복
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크크
        if event.type == pygame.QUIT: #창 닫는 이벤트트
            running = False
        pygame.draw.circle(screen, (200, 155, 110), (200, screen_height / 2), 172)
        pygame.draw.circle(screen, (60, 100, 220), (470, screen_height / 2), 61)
        pygame.draw.circle(screen, (215, 190, 135), (700, screen_height / 2), 143)
        pygame.draw.circle(screen, (70, 130, 210), (900, screen_height / 2), 16)
        pygame.draw.circle(screen, (225, 195, 125), (1050, screen_height / 2), 15)
        pygame.draw.circle(screen, (0, 225, 100), (1200, screen_height / 2), 62)
        pygame.draw.circle(screen, (0, 225, 100), (1350, screen_height / 2), 6)
        pygame.draw.circle(screen, (0, 225, 100), (1500, screen_height / 2), 8)
    

    pygame.display.update()
#종료처리
pygame.quit()