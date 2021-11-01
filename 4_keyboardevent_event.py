import pygame

pygame.init() # 초기화 반드시 필요 -> 'pygame' 사용 시 반드시 선언


#화면 크기 설정
screen_width = 480 #가로 
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game Project") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:\\devtools\\pythonworkspace\\first_python_project\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\devtools\\pythonworkspace\\first_python_project\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해줌
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는곳에 위치

#키보드 이동 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임 진행 여부
while running:
    #이 부분도 'pygame' 사용 시 반드시 필요하다 몰라도 된다. 적기만 하자
    for event in pygame.event.get(): #event.get()을 통해 사용자의 움직임을 받음
        if event.type == pygame.QUIT: #창의 x버튼
            running = False

        if event.type == pygame.KEYDOWN: #키보드 누르는 이벤트
            if event.key == pygame.K_LEFT:#키보드 방향
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP: #키보드를 멈추는 이벤트
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #캐릭터 이동 후 좌표
    character_x_pos += to_x
    character_y_pos += to_y

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0)) #x, y 좌표로 blit()가 배경을 그린다. 

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #화면을 계속해서 그려주는 함수


# 게임 종료시 pygame 종료
pygame.quit()