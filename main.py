from config_reader import ConfigReader
from data_saver import DataSaver
from ferromagnetic_nanoparticle import FerromagneticNanoparticle

INPUT_CONFIG = "data/input.cfg"
LOG_FILE = "data/log.txt"
M_MOMENT_FILE = "data/mMoment.txt"
P_BODY_FILE = "data/pBody.txt"

config_reader = ConfigReader(INPUT_CONFIG)

config_reader.read_file()
config_data = config_reader.data

data_saver = DataSaver(LOG_FILE, P_BODY_FILE, M_MOMENT_FILE, config_data)
data_saver.create_log_file()
data_saver.write_result()
data_saver.write_additional_result()

ferromagnetic_nanoparticle = FerromagneticNanoparticle(config_data)
print(ferromagnetic_nanoparticle.magnetization)
print(ferromagnetic_nanoparticle.viscosity)
print(ferromagnetic_nanoparticle.alpha)
print(ferromagnetic_nanoparticle.amplitude)
print(ferromagnetic_nanoparticle.time)
print(ferromagnetic_nanoparticle.dt)
print(ferromagnetic_nanoparticle.small_theta)
print(ferromagnetic_nanoparticle.small_phi)
print(ferromagnetic_nanoparticle.big_theta)
print(ferromagnetic_nanoparticle.big_phi)
print(ferromagnetic_nanoparticle.rho)
ferromagnetic_nanoparticle.calc_parameters()
print(ferromagnetic_nanoparticle.alpha_1)
print(ferromagnetic_nanoparticle.beta)
print(ferromagnetic_nanoparticle.beta_1)
print(ferromagnetic_nanoparticle.tau_1)
print(ferromagnetic_nanoparticle.tau_2)
