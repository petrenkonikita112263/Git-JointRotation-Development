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
ferromagnetic_nanoparticle.calc_parameters()
time, dt = ferromagnetic_nanoparticle.calc_time_parameters()
ferromagnetic_nanoparticle.calc_main_func(time)
ferromagnetic_nanoparticle.calc_energy(time)
