
import pandas as pd

df = pd.read_csv("datos/ventas.csv")

df["Venta_Total"] = df["Cantidad"] * df["Precio"]

total_vendido = df["Venta_Total"].sum()
promedio_ventas = df["Venta_Total"].mean()

producto_mas_vendido = (
    df.groupby("Producto")["Cantidad"]
    .sum()
    .idxmax()
)

ventas_categoria = (
    df.groupby("Categoria")["Venta_Total"]
    .sum()
)

print("TOTAL VENDIDO:", total_vendido)
print("PROMEDIO:", promedio_ventas)
print("PRODUCTO MÁS VENDIDO:", producto_mas_vendido)

print("\nVENTAS POR CATEGORIA")
print(ventas_categoria)
