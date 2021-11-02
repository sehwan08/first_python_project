import pygame
import random

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

background = pygame.image.load("C:\\devtools\\pythonworkspace\\first_python_project\\background.jpg")

#2. 캐릭터 만들기
character = pygame.image.load("C:\\devtools\\pythonworkspace\\first_python_project\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해줌
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는곳에 위치

#7 적 만들기
enemy = pygame.image.load("C:\\devtools\\pythonworkspace\\first_python_project\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해줌
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10



#3. 키보드 이벤트
to_x = 0
to_y = 0
character_speed = 10

#4. 이벤트 루프
running = True #게임 진행 여부
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    #5. 키보드 이벤트 처리 
    for event in pygame.event.get(): #event.get()을 통해 사용자의 움직임을 받음
        if event.type == pygame.QUIT: #창의 x버튼
            running = False

        if event.type == pygame.KEYDOWN: #키보드 누르는 이벤트
            if event.key == pygame.K_LEFT:#키보드 방향
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP: #키보드를 멈추는 이벤트
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0





    #6. 게임 캐릭터 위치 (가로/세로 경계값)
    #캐릭터 이동 후 좌표
    character_x_pos += to_x 
    character_y_pos += to_y 

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed 

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width-enemy_width)


    #8. 충돌 처리
    character_rect = character.get_rect() #케릭터의 좌표,넓이,높이를 가지고 있음
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("Crushed!")
        running = False


    #6. 화면에 그리기 (.blit)
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    #타이머 집어 넣기 ( 경과 시간 )

    # 글자 실제 반영 (시간, True, 글자 색상 (*고정))

    # 시간 처리

    pygame.display.update() #화면을 계속해서 그려주는 함수

#시간 오버 게임 종료시 약간의 텀을 주고 종료
pygame.time.delay(2000)

# 게임 종료시 pygame 종료
pygame.quit()