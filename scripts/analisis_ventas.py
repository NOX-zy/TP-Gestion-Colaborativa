#KAN-2 feat: Lectura de csv y carga en dataframe
import pandas as pd

df = pd.read_csv("datos/ventas.csv")

print(df.head())


#KAN-3 feat:

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
    df.groupby("Categoría")["Venta_Total"]
    .sum()
)

print("TOTAL VENDIDO:", total_vendido)
print("PROMEDIO:", promedio_ventas)
print("PRODUCTO MÁS VENDIDO:", producto_mas_vendido)

print("\nVENTAS POR CATEGORÍA")
print(ventas_categoria)


#Grafico
import matplotlib.pyplot as plt

# Crear columna de venta total
df["Venta_Total"] = df["Cantidad"] * df["Precio"]

# Mostrar primeras filas
print(df.head())

# Ventas por categoría
ventas_categoria = df.groupby("Categoría")["Venta_Total"].sum()

# Crear gráfico
plt.figure(figsize=(8,5))
ventas_categoria.plot(kind="bar")

plt.title("Ventas por categoria")
plt.xlabel("Categoria")
plt.ylabel("Ventas")

plt.tight_layout()

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Grafico guardado correctamente")
