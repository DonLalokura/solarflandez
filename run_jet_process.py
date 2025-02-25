from jet_process import intensity_process

# Seleccionar el jet
jet_name = "jet_1"

# Definir las rutas basadas en el jet seleccionado
input_folder = "data-193"
stats_file = f"{jet_name}_stats.npy"
output_dir = f"{jet_name}_images"

# Llamar a la función usando el nombre del jet
intensity_process(jet_name, input_folder, stats_file, output_dir)
