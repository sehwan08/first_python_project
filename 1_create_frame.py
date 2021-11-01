import pygame

pygame.init() # 초기화 반드시 필요 -> 'pygame' 사용 시 반드시 선언


#화면 크기 설정
screen_width = 480 #가로 
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game Project") #게임 이름

#이벤트 루프
running = True #게임 진행 여부
while running:
    #이 부분도 'pygame' 사용 시 반드시 필요하다 몰라도 된다. 적기만 하자
    for event in pygame.event.get(): #event.get()을 통해 사용자의 움직임을 받음
        if event.type == pygame.QUIT: #창의 x버튼
            running = False


# 게임 종료시 pygame 종료
pygame.quit()