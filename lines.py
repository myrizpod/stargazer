import pygame
import constants as ct
import maths as t

def basic(start,end,col):
    pygame.draw.line(ct.RENDER_BUFFER,col,start,end)
    
def double(start,end,col):
    v = (end[0]-start[0],end[1]-start[1])
    v = t.perp_vec(t.normalize(v))
    pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]+v[0],start[1]+v[1]),(end[0]+v[0],end[1]+v[1]))
    pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]-v[0],start[1]-v[1]),(end[0]-v[0],end[1]-v[1]))
    
def triple(start,end,col):
    v = (end[0]-start[0],end[1]-start[1])
    v = t.perp_vec(t.normalize(v,2))
    pygame.draw.line(ct.RENDER_BUFFER,col,start,end)
    pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]+v[0],start[1]+v[1]),(end[0]+v[0],end[1]+v[1]))
    pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]-v[0],start[1]-v[1]),(end[0]-v[0],end[1]-v[1]))

def dash(start,end,col):
    v = (end[0]-start[0],end[1]-start[1])
    l = t.dist(0,0,v[0],v[1])
    v1 = t.normalize(v,7)
    v2 = t.normalize(v,15)
    for i in range(int(l/15+0.8)):
        pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]+v2[0]*(i),start[1]+v2[1]*(i)),(start[0]+v2[0]*(i)+v1[0],start[1]+v2[1]*(i)+v1[1]))
        
def short_dash(start,end,col):
    v = (end[0]-start[0],end[1]-start[1])
    l = t.dist(0,0,v[0],v[1])
    v1 = t.normalize(v,3)
    v2 = t.normalize(v,8)
    for i in range(int(l/8+1)):
        pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]+v2[0]*(i),start[1]+v2[1]*(i)),(start[0]+v2[0]*(i)+v1[0],start[1]+v2[1]*(i)+v1[1]))
        
        
def add_marker(start, end, col, func, additional_func=None, additional=None, start_mark=True, end_mark=True):
    v = (end[0]-start[0],end[1]-start[1])
    v = t.normalize(v,5)
    if start_mark:
        pygame.draw.rect(ct.RENDER_BUFFER,col,pygame.Rect(start[0]-1,start[1]-1,3,3),1,1)
    if end_mark:
        pygame.draw.rect(ct.RENDER_BUFFER,col,pygame.Rect(end[0]-1,end[1]-1,3,3),1,1)
    if additional is not None:
        func((start[0]+v[0],start[1]+v[1]), (end[0]-v[0],end[1]-v[1]), col, additional_func, additional)
    else:
        func((start[0]+v[0],start[1]+v[1]),(end[0]-v[0],end[1]-v[1]),col)
    
    
def addbroken(start,end,col,func,level):
    v = (end[0]-start[0],end[1]-start[1])
    l = t.dist(0,0,v[0],v[1])
    perp = t.perp_vec(t.normalize(v,3))
    smol_v = t.normalize(v,3)
    v = t.normalize(v,(l-3*level-3)/2)
    func((start[0],start[1]),(start[0]+v[0],start[1]+v[1]),col)
    func((end[0]-v[0],end[1]-v[1]),(end[0],end[1]),col)
    for i in range(level):
        i+=1
        pygame.draw.line(ct.RENDER_BUFFER,col,(start[0]+v[0]+smol_v[0]*i+perp[0],start[1]+v[1]+smol_v[1]*i+perp[1]),(start[0]+v[0]+smol_v[0]*i-perp[0],start[1]+v[1]+smol_v[1]*i-perp[1]))
        
def link_displace(start,end):
    v = (end[0]-start[0],end[1]-start[1])
    v = t.normalize(v,8)
    return (start[0]+v[0],start[1]+v[1]),(end[0]-v[0],end[1]-v[1])
    