from PIL import Image

color_str = "wmzвгдеёжзийклмнопрсoahkbdpqjftZO0QLCJUYX/\|()1{}[]?-_+~i!lI;:,\"^`'. "
ascii_char = list(color_str)

unit = 256 / len(ascii_char)
print(len(ascii_char))