import pygame
pygame.init() # 초기화 반드시 필요 -> 'pygame' 사용 시 반드시 선언

#화면 크기 설정
screen_width = 480 #가로 
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game Project") #게임 이름

#FPS
clock = pygame.time.Clock()

####################################################################################

#1.사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 시간 등)


#2. 이벤트 루프
running = True #게임 진행 여부
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    #3. 이벤트 처리 
    #print("FPS: "+str(clock.get_fps())) # 프레임 속도 확인
    #이 부분도 'pygame' 사용 시 반드시 필요하다 몰라도 된다. 적기만 하자
    for event in pygame.event.get(): #event.get()을 통해 사용자의 움직임을 받음
        if event.type == pygame.QUIT: #창의 x버튼
            running = False


    #4. 게임 캐릭터 위치 (가로/세로 경계값)


    #5. 충돌 처리


  
        running = False

    #6. 화면에 그리기 (.blit)

    #타이머 집어 넣기 ( 경과 시간 )

    # 글자 실제 반영 (시간, True, 글자 색상 (*고정))

    # 시간 처리

    pygame.display.update() #화면을 계속해서 그려주는 함수

#시간 오버 게임 종료시 약간의 텀을 주고 종료
pygame.time.delay(2000)

# 게임 종료시 pygame 종료
pygame.quit()