class Tamagotchi:
    def __init__(self, nombre, nivel_energia= 100, nivel_hambre= 0, nivel_felicidad= 50,  esta_vivo=True):        
        self.nombre = nombre
        self.nivel_energia = nivel_energia
        self.nivel_hambre = nivel_hambre
        self.nivel_felicidad = nivel_felicidad        
        self.esta_vivo = esta_vivo 
        self.actualizar_humor()       
                
    def hambre(self):
        estado_hambre= {1:"nada", 2:"poco", 3:"mucho"}
        hambre_respuesta= ""                     
        if self.nivel_hambre <= 40:
            hambre_respuesta = estado_hambre[2]
        elif self.nivel_hambre >40 and self.nivel_hambre < 60:
            hambre_respuesta = estado_hambre[2]
        elif self.nivel_hambre >= 60 :    
            hambre_respuesta = estado_hambre[3]
        return  hambre_respuesta             
    
    def actualizar_humor(self):
        if self.nivel_felicidad >= 80:
            self.humor = "eufórico"
        elif self.nivel_felicidad >= 60:
            self.humor = "feliz"
        elif self.nivel_felicidad >= 40:
            self.humor = "indiferente"
        elif self.nivel_felicidad >= 20:
            self.humor = "triste"
        else:
            self.humor = "enojado"            
                
    def mostrar_estado(self):
        print(f"Me llamo {self.nombre},  estoy con {self.nivel_energia} de energía, estoy con {self.nivel_energia} nivel de hambre, y estoy {self.humor}")
    
    def alimentar(self):
        if self.esta_vivo:
            self.nivel_hambre = max(0, self.nivel_hambre - 10)
            self.nivel_energia = max(0, self.nivel_energia - 15)
            self.verificar_estado()                       
    def jugar(self):
        if self.esta_vivo:
            self.nivel_felicidad +=20
            self.nivel_hambre += 10
            self.nivel_energia = max(0, self.nivel_energia - 18)
            self.verificar_estado()
    
    def dormir(self):
        if self.esta_vivo:
            self.nivel_energia += 40
            self.nivel_hambre +=5
            self.verificar_estado()
        
    def verificar_estado(self):
        if self.nivel_hambre >= 20:
            self.nivel_energia = max(0, self.nivel_energia - 20)
            self.nivel_felicidad = max(0, self.nivel_felicidad - 30)

        if self.nivel_energia <= 0:
            self.esta_vivo = False

        self.actualizar_humor()
        
    def estado_vital(self):
     estado = "vivo" if self.esta_vivo else "muerto"
     return estado
     
            
            
mi_tamagotchi = Tamagotchi("Tama")
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.alimentar()
mi_tamagotchi.alimentar()
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.jugar()
mi_tamagotchi.jugar()
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.dormir()
mi_tamagotchi.dormir()
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.jugar()
mi_tamagotchi.jugar()
mi_tamagotchi.jugar()
mi_tamagotchi.jugar()
mi_tamagotchi.jugar()

mi_tamagotchi.mostrar_estado()
print(mi_tamagotchi.estado_vital())