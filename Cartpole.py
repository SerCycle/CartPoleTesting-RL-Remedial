# import module gym
import gym

# membuat environment untuk cartpole
env = gym.make('CartPole-v1')

# membuat inputan untuk perulangan episode atau percobaan
percobaan = int(input("masukkan banyak percobaan: "))
keputusan =[]

# membuat sebuah sistem yang dimana akan digunakan untuk perulangan percobaan
for i_episode in range(percobaan):
    
    # mereset observasi sebagai titik ulang percobaan pada cartpole
    observation = env.reset()

    # membuat perulangan sebagai keputusan atau action yang harus dilakukan
    for t in range(100):

        # melakukan rendering sebuah keputasan menjadi matrix
        env.render()

        # memberikan sebuah variable untuk action yang diisi oleh beberapa sample bawaan library
        action = env.action_space.sample()

        # split data mengenai step untuk action yang dilakukan
        observation, reward, done, info = env.step(action)

        # decision making ketika sudah selesai
        if done:
            print("Episode", i_episode+1, "finished after {} timesteps".format(t+1))
            keputusan.append(t+1)
            break

# menutup environtment
env.close()
keputusan.sort(reverse=True)
print("Action terbanyak yang dilakukan oleh cartpole untuk menyeimbangkan adalah", keputusan[0], "kali")