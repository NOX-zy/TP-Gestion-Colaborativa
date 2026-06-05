#KAN-2 feat: Lectura de csv y carga en dataframe
import pandas as pd

df = pd.read_csv("datos/ventas.csv")

print(df.head())

import pandas as pd


#KAN-3 feat:
df = pd.read_csv("datos/ventas.csv")

# Crear columna de venta total
df["Venta_Total"] = df["Cantidad"] * df["Precio"]

# Total vendido
total_vendido = df["Venta_Total"].sum()

# Promedio
promedio_ventas = df["Venta_Total"].mean()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("Producto")["Cantidad"]
    .sum()
    .idxmax()
)

# Ventas por categoría
ventas_categoria = (
    df.groupby("Categoria")["Venta_Total"]
    .sum()
)

print("TOTAL VENDIDO:", total_vendido)
print("PROMEDIO:", promedio_ventas)
print("PRODUCTO MÁS VENDIDO:", producto_mas_vendido)

print("\nVENTAS POR CATEGORÍA")
print(ventas_categoria)
