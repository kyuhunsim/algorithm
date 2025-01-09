# import control
# import numpy as np
# import matplotlib.pyplot as plt

# # Define the transfer function of the system
# num = [1]
# den = [1, 10, 20]
# system = control.TransferFunction(num, den)

# # Define the PID controller
# Kp = 1
# Ki = 0
# Kd = 0
# pid = control.TransferFunction([Kd, Kp, Ki], [1, 0])

# # Create the closed-loop system
# closed_loop_system = control.feedback(pid * system)

# # Time vector
# t = np.linspace(0, 5, 500)

# # Step response
# t, y = control.step_response(closed_loop_system, t)

# # Plot the step response
# plt.figure()
# plt.plot(t, y)
# plt.title('Step Response with PID Controller')
# plt.xlabel('Time (s)')
# plt.ylabel('Response')
# plt.grid(True)
# plt.show()
