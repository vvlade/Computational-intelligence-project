import numpy as np
from tqdm import tqdm
import test_functions as test

class Particle:
    global_best_value = None
    global_best_position = None
    
    def __init__(self, obj_func, bounds, c_i, c_s, c_c):
        self.obj_function = obj_func
        self.c_i = c_i
        self.c_c = c_c
        self.c_s = c_s
        
        self.lower_bounds = np.array([bound[0] for bound in bounds])
        self.upper_bounds = np.array([bound[1] for bound in bounds])
        
        self.position = np.random.uniform(self.lower_bounds, self.upper_bounds, len(bounds))
        self.value = self.obj_function(self.position)
        
        self.personal_best_position = self.position.copy()
        self.personal_best_value = self.value
        
        self.velocity = np.random.uniform(self.lower_bounds - self.upper_bounds,
                                          self.upper_bounds - self.lower_bounds,
                                          len(bounds))
        
        if Particle.global_best_value is None or self.value < Particle.global_best_value:
            Particle.global_best_position = self.position.copy()
            Particle.global_best_value = self.value
        
    
    def update_velocity(self):
        r_c = np.random.random(self.velocity.shape)
        r_s = np.random.random(self.velocity.shape)
        
        cognitive_velocity = r_c * self.c_c * (self.personal_best_position - self.position)
        social_velocity    = r_s * self.c_s * (Particle.global_best_position - self.position)
        inertia            = self.c_i * self.velocity
        
        self.velocity = cognitive_velocity + social_velocity + inertia
    
    def update_position(self):
        self.position = np.clip(self.position + self.velocity, self.lower_bounds, self.upper_bounds)
        self.value = self.obj_function(self.position)
        
        if self.value < self.personal_best_value:
            self.personal_best_value = self.value
            self.personal_best_position = self.position.copy()
            
            if self.value < Particle.global_best_value:
                Particle.global_best_value = self.value
                Particle.global_best_position = self.position.copy()
    
    
def PSO(swarm_size, num_iters, c_i, c_c, c_s, obj_func, num_dimensions, lb, ub):
    bounds = [(lb, ub) for _ in range(num_dimensions)]
    swarm = [Particle(obj_func, bounds, c_i, c_s, c_c) for _ in range(swarm_size)]
    
    for iter in tqdm(range(num_iters)):
        for particle in swarm:
            particle.update_velocity()
            particle.update_position()
        
    print(f'Global best value: {Particle.global_best_value}')
    print(f'Global best position: {Particle.global_best_position}')
        
    Particle.global_best_position = None
    Particle.global_best_value = None