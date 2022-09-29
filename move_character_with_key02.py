from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global dyr
    global k # 캐릭터가 진행하는 방향 구분

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                k = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                k = -1
            elif event.key == SDLK_UP:
                dyr += 1
            elif event.key == SDLK_DOWN:
                dyr -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dyr -= 1
            elif event.key == SDLK_DOWN:
                dyr += 1
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
dyr = 0
k=0

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if k == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif k == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif k == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += dyr * 5


    delay(0.01)

close_canvas()

