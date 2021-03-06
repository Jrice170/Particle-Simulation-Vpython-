## Joseph Rice



# 12/29/2017



import datetime



from time import sleep



from visual import *



from visual.graph import *



from random import *







"""isocalendar(...)"""



"""Return a 3-tuple containing ISO year, week number, and weekday."""



now = datetime.datetime.today()



print(now)



# print(date.ioscalendar(now.year,now.week,now.weekday))



format_e = datetime.date(now.year,now.month,now.day).isocalendar()



print(format_e)



print('\ndirections:\n','\nleft click and hold to move screen\n',\



'\nhold both left and right to zoom in and out\n')



scene.width = 1000



scene.height = 1000



scene.title = "_diffusion_"



## 1 change direction of vector be that x y or z or both

Graph = gdisplay(x=0,y=0,width=600,height=150,title= "Distance Vs Time",\

                 xtitle="Time",ytitle="Distance",foreground=color.white,background=color.black)

b1 = gcurve(color = color.red)

b2 = gcurve(color = color.cyan)

b3 = gcurve(color = color.yellow)

b4 = gcurve(color = color.blue)

b5 = gcurve(color = color.magenta)

b6 = gcurve(color = color.green)

b7 = gcurve(color = color.orange)

b8 = gcurve(color = color.white)





class atoms:



    def __init__(self,x,y,z,radius,color,vector):



        """" x pos, y pos, z pos, radius, color , vector from list"""



        self.x,self.y,self.z,self.radius,self.color = x,y,z,radius,color,



        self.ball,self.ball.velocity = sphere(pos=(self.x,self.y,self.z),\



        radius=self.radius,\



        color=self.color,make_trail=True,trail_type="points",\



        meterial=materials.emissive),vector







    def random_move(self,speed):



        speed,value = 5*random()*speed/2,randrange(0,16)



        if value == 1:



            self.ball.pos.x +=  self.ball.velocity.x*speed



        elif value ==2:



            self.ball.pos.y +=  self.ball.velocity.y*speed



        elif value ==3:



            self.ball.pos.z += self.ball.velocity.z*speed



        elif value ==4:



            self.ball.pos.x +=  self.ball.velocity.x*speed



            self.ball.pos.y += self.ball.velocity.y*speed



        elif value ==5:



            self.ball.pos.x +=  self.ball.velocity.x*speed



            self.ball.pos.z +=  self.ball.velocity.z*speed



        elif value ==6:



            self.ball.pos.y +=  self.ball.velocity.y*speed



            self.ball.pos.z +=  self.ball.velocity.z*speed



        elif value ==7:



            self.ball.pos.x +=  self.ball.velocity.x*speed



            self.ball.pos.y +=  self.ball.velocity.y*speed



        elif value ==8:



            self.ball.pos.x +=  self.ball.velocity.x*speed



            self.ball.pos.z += self.ball.velocity.z*speed



        elif value ==9:



            self.ball.pos.z +=  + self.ball.velocity.z*speed



            self.ball.pos.y +=  + self.ball.velocity.y*speed



        elif value ==10:



            self.ball.velocity.x = -self.ball.velocity.x



            self.ball.pos.x +=  self.ball.velocity.x * speed



        elif value ==11:



            self.ball.velocity.y = -self.ball.velocity.y



            self.ball.pos.y +=  self.ball.velocity.y*speed



        elif value ==12:



            self.ball.velocity.z = -self.ball.velocity.z



            self.ball.pos.z +=  self.ball.velocity.z*speed



        elif value ==13:



            self.ball.velocity = -self.ball.velocity



            self.ball.pos +=  self.ball.velocity*speed



        else:



            self.ball.pos.x +=  self.ball.velocity.x*speed



            self.ball.pos.y +=  self.ball.velocity.y*speed



            self.ball.pos.z +=  self.ball.velocity.z*speed



    def distance(self):

        # x, y, z, put as object.x ect

        # ball_object.pos.x current position

        calculate = ((self.x-self.ball.pos.x)**2 + (self.y-self.ball.pos.y)**2 + (self.z-self.ball.pos.z)**2)

        distance_from_start = sqrt(calculate)

        return distance_from_start



       



list = [vector(2,2,2),vector(-2,2,2),vector(2,-2,2),vector(2,2,-2),vector(-2,-2,2),\



vector(-2,-2,-2),vector(-2,2,-2),vector(-2,-2,2)]



color = [color.red,color.cyan,color.yellow,color.blue,color.magenta,color.green,\



color.orange,color.white]



value1,value2,value3,value4,value5,value6,value7,value8=randrange(0,8),randrange(0,8),randrange(0,8),randrange(0,8),randrange(0,8),randrange(0,8),randrange(0,8),randrange(0,8)







radius = 0.5



atom_list = [atoms(radius,5,-10,-5,color[0],list[value1]),\



atoms(radius,5,-10,-5,color[1],list[value2]),atoms(radius,5,-10,-5,color[2],list[value3]),\



atoms(radius,5,-10,-5,color[3],list[value4]),atoms(radius,5,-10,-5,color[4],\



list[value5]),atoms(radius,5,-10,-5,color[5],list[value6]),atoms(radius,5,-10,-5,\



color[6],list[value7]),atoms(radius,5,-10,-5,\



color[7],list[value8])]



ball,ba11,ba12,ba13,ba14,bal5,bal6,bal7 = atom_list[0],atom_list[1],atom_list[2],atom_list[3],atom_list[4],atom_list[5],atom_list[6],atom_list[7]







def main():



    time = (int(input("how long do you what the simulation to run (seconds): ")))







    Clock = 0



    start = input("Enter to start: ")



    print('5 seconds....')



    # 5 seconds to get started



    sleep(5)







    while start =='':



        



        Clock += 0.001



        ball.random_move(0.1)

        b1.plot(pos=(Clock,ball.distance()))

        

        

        ba12.random_move(0.1)

        b2.plot(pos=(Clock,ba12.distance()))



        ba13.random_move(0.1)

        b3.plot(pos=(Clock,ba13.distance()))



        ba14.random_move(0.1)

        b4.plot(pos=(Clock,ba14.distance()))

        

        bal5.random_move(0.1)

        b5.plot(pos=(Clock,bal5.distance()))



        bal6.random_move(0.1)

        b6.plot(pos=(Clock,bal6.distance()))



        bal7.random_move(0.1)

        b7.plot(pos=(Clock,bal7.distance()))



        



        if Clock >= time:



            break



main()
