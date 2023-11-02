"""
11bfi_42o:0zazL:vvs:::
"""
screen.fill((0,0,0))
app.text0.configure(bg="black", fg="white", insertbackground="red", width=80)
cap0.canvas.configure(bg="black", width=418, height=418)
cap0.canvas.delete("all")
laa = _urL_ns104(204, 418, 13)
la = laa[13:37]
cap0.canvas.create_polygon(la, fill="red")
sula = ""
soa = szfy.so
l_sula = []
for i_ in la:
    l_sula.append(i_ % 36)
    
for i_ in l_sula:
    sula += soa[i_]
#print(sula)
if "god" in sula:
    pass
    #print(sula)
    
screen.blit( font.render(f"{sula}", True, (255,255,0)), (13, 193) )
#----------pg

pg.draw.circle(screen, (255,0,0), (208, 208), 13, 3)
#---
screen.set_at((213, 213), (255,255,255))
#screen = pg.display.set_mode((418, 418), 0, 32)
if s_Text:
    screen.blit( font.render(f"{s_Text}", True, (255,255,0)), (13, 36) )
    lucy = uxlife(s_Text)
    if lucy:
       screen.blit( font.render(f"{lucy[0:2]}", True, (0,255,0)), (13, 93) ) 
       #screen.blit( font.render(f"ok", True, (255,255,0)), (13, 193) )
#---
FPS = 60


