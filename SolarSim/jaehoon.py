#-*- coding: utf-8 -*-
import pygame

pygame.init() #초기화 (반드시 필요)

#화면크기 설정
screen_width = 1600
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

font =  pygame.font.SysFont("malgungothic", 28)
big_font =  pygame.font.SysFont("malgungothic", 50)
small_font =  pygame.font.SysFont("malgungothic", 17)

#화면 타이틀 (제목창)
pygame.display.set_caption("코딩쌤 초미남")

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인

while running: # 반복
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크크
        if event.type == pygame.QUIT: #창 닫는 이벤트트
            running = False
        pygame.draw.circle(screen, (216, 202, 167), (200, screen_height / 2), 172)
        pygame.draw.circle(screen, (91, 93, 223), (470, screen_height / 2), 61)
        pygame.draw.circle(screen, (234, 214, 184), (700, screen_height / 2), 143)
        pygame.draw.circle(screen, (43, 130, 201), (900, screen_height / 2), 16)
        pygame.draw.circle(screen, (227, 187, 118), (1050, screen_height / 2), 15)
        pygame.draw.circle(screen, (172, 229, 238), (1200, screen_height / 2), 62)
        pygame.draw.circle(screen, (193, 68, 14), (1350, screen_height / 2), 6)
        pygame.draw.circle(screen, (169, 169, 169), (1500, screen_height / 2), 8)

        screen.blit(big_font.render("행성별 표면 중력 비교",True,(255,255,255)),(600,50))
        screen.blit(font.render("목성",True,(255,255,255)),(170,550))
        screen.blit(font.render("해왕성",True,(255,255,255)),(425,550))
        screen.blit(font.render("토성",True,(255,255,255)),(660,550))
        screen.blit(font.render("지구",True,(255,255,255)),(870,550))
        screen.blit(font.render("금성",True,(255,255,255)),(1025,550))
        screen.blit(font.render("천왕성",True,(255,255,255)),(1160,550))
        screen.blit(font.render("화성",True,(255,255,255)),(1325,550))
        screen.blit(font.render("수성",True,(255,255,255)),(1475,550))
        screen.blit(small_font.render("약 24.8 m/s²",True,(255,255,255)),(150,600))
        screen.blit(small_font.render("약 11.2 m/s²",True,(255,255,255)),(420,600))
        screen.blit(small_font.render("약 10.4 m/s²",True,(255,255,255)),(650,600))
        screen.blit(small_font.render("약 9.8 m/s²",True,(255,255,255)),(860,600))
        screen.blit(small_font.render("약 8.9 m/s²",True,(255,255,255)),(1005,600))
        screen.blit(small_font.render("약 8.7~8.9 m/s²",True,(255,255,255)),(1140,600))
        screen.blit(small_font.render("약 3.7 m/s²",True,(255,255,255)),(1305,600))
        screen.blit(small_font.render("약 3.7 m/s²",True,(255,255,255)),(1455,600))
    

    pygame.display.update()
#종료처리
pygame.quit()