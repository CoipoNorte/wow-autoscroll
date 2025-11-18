# ⚔️ WoW Auto-Scroll

Herramienta minimalista para automatizar SHIFT + Scroll en World of Warcraft.

![Version](https://img.shields.io/badge/version-1.0-green)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

---

## 📖 ¿Qué hace?

Esta aplicación automatiza la acción repetitiva de **SHIFT + Scroll** (arriba y abajo alternado) a una velocidad fija de **2 scrolls por segundo**.

Perfecto para actividades en WoW que requieren mantener presionada esta combinación por períodos largos (como hacer zoom de cámara repetidamente o spam de habilidades mapeadas al scroll).

---

## 🎮 Características

✅ **Interfaz ultra minimalista** - Botón circular de 30x30 píxeles (tamaño de habilidad WoW)  
✅ **Siempre visible** - Se mantiene sobre todas las ventanas  
✅ **Arrastrable** - Mueve el botón donde quieras  
✅ **Sin ventana de consola** - Totalmente discreto  
✅ **Indicador visual** - Punto rojo (inactivo) / verde (activo)  
✅ **Controles simples** - Solo 3 acciones posibles

---

## 🚀 Uso

### Inicio rápido:
1. Ejecuta `WoW_AutoScroll.exe`
2. Aparecerá un pequeño círculo verde en la esquina superior izquierda (posición 100, 100)
3. Arrastra el círculo a donde prefieras (se queda siempre encima de todas las ventanas)

---

## 🎯 Controles

| Acción | Control |
|--------|---------|
| **Activar/Desactivar** | Presiona `C` o haz **clic izquierdo** en el círculo |
| **Mover el botón** | **Clic izquierdo** + arrastrar |
| **Cerrar programa** | **Clic derecho** en el círculo |

---

## 🔴🟢 Indicadores visuales

| Estado | Apariencia |
|--------|------------|
| **⚫ Inactivo** | Círculo gris con punto rojo en el centro |
| **🟢 Activo** | Círculo verde oscuro con punto verde brillante |

---

## ⚙️ Especificaciones técnicas

- **Acción**: SHIFT + Scroll (arriba/abajo alternado)
- **Velocidad**: 2 scrolls por segundo (intervalo de 0.5s)
- **Patrón**: Alternado (⬆️ arriba → ⬇️ abajo → ⬆️ arriba → ⬇️ abajo...)
- **Tamaño**: 30x30 píxeles
- **Posición inicial**: X:100, Y:100 (esquina superior izquierda)
- **Siempre encima**: Sí

---

## 🔧 Modificar la velocidad

Si necesitas cambiar la velocidad, edita el archivo `wow_autoscroll.py` en la **línea 11**:

```python
self.scroll_interval = 0.5  # 2 scrolls/segundo

# Ejemplos:
# 0.33 = 3 scrolls/segundo
# 0.25 = 4 scrolls/segundo  
# 0.2  = 5 scrolls/segundo
# 0.1  = 10 scrolls/segundo

```
## Compilar
```python
pyinstaller --onefile --noconsole --name "WoW_AutoScroll" wow_autoscroll.py

pyinstaller --onefile --noconsole --icon=wow_scroll.ico --name "WoW_AutoScroll" wow_autoscroll.py
```