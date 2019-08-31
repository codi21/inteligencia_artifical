# Agentes Racionales

## Implementación de agente racional reactivo.
> El agente racional reactivo implementado en python , su método principal (think) , está guiado según la localización del mismo.
> Éste se mueve hacia la derecha o izquierda según si la fila en el que se encuentra es par ó impar.
> Así mismo el otro agente solicitado en el trabajo práctico se mueve aleatoriamente según el valor arrojado por la función randomint.

## Evaluacion de resultados
### Agente reflexivo simple con think configurado
| Entorno/ Porcentaje de suciedad | 2x2 | 4x4  | 8x8   | 16x16   | 32x32   | 64x64    | 128x128   |
|---------------------------------|-----|------|-------|---------|---------|----------|-----------|
| %10                             | 0/0 | 1/2  | 3/6   | 16/26   | 66/683  | 87/410   | 117/1683  |
| %20                             | 1/1 | 2/3  | 6/13  | 33/51   | 127/205 | 196/819  | 232/3277  |
| %40                             | 2/2 | 4/6  | 15/20 | 68/102  | 255/410 | 397/1639 | 426/6554  |
| %80                             | 2/3 | 7/13 | 31/51 | 136/205 | 540/819 | 793/3277 | 814/13107 |

### Agente reflexivo simple con think aleatorio
| Entorno/ Porcentaje de suciedad | 2x2 | 4x4   | 8x8   | 16x16   | 32x32   | 64x64    | 128x128   |
|---------------------------------|-----|-------|-------|---------|---------|----------|-----------|
| %10                             | 0/0 | 2/2   | 6/6   | 23/26   | 32/102  | 37/410   | 34/1638   |
| %20                             | 1/1 | 3/3   | 13/13 | 41/51   | 64/205  | 86/819   | 76/3277   |
| %40                             | 2/2 | 6/6   | 26/27 | 87/102  | 131/410 | 90/1738  | 161/6554  |
| %80                             | 3/3 | 13/13 | 51/51 | 160/206 | 128/819 | 226/3277 | 338/13107 |

>2.9
>a)En el caso que se penalizara al agente por cada vez que haga un movimiento , éste sería irracional(Agente reflexivo simple)
>porque eso no le impediria volver a recorrer caminos ya vistos anteriormente.
>b)Para un agente con estado seria racional, ya que sabría que caminos recorrio previamente.
>c)Si ya que poseería conocimiento del medio en el que se va a mover. Bajo la medida de rendimiente que se propone
>éste va a elegir la mejor opción según donde esté parado.

>2.10
>a) Un agente reactivo simple en el caso de estar en un medio totalmente desconocido sería muy irracional porque no sabría como
>actuar frente a determinados obstaculos ó limites del mapa.
>b)Según la medida de rendimiento propuesta. Por ejemplo en el caso que implemente yo un agente aleatorio para matrices pequeñas
>no dejaba suciedad pero ocupaba todos los periodos de vida. Y para el caso en el que le configure patrones a seguir este obtuvo mejores
>resultados en matrices grandes.
>c)En los experimentos realizados tras analizar los valores cabe destacar que el agente aleatorio en matrices grandes limpió demasiado poco.
>d)Si ya que sabría porque posiciones ya ha pasado.