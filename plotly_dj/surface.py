
import plotly.graph_objects as go

def anisurf(Z_t,title="",zmin=0,zmax=6,duration=5):
    fig = go.Figure()

    # Animación
    Nt = Z_t.shape[2]
    frames = []
    for it in range(Nt):  # Valores de tiempo de 0 a 2 en 30 pasos
        if it ==0:
            fig.add_traces(go.Contour(z=Z_t[:,:,it], colorscale='jet', showscale=True,zmin=zmin, zmax=zmax))

        frames.append(go.Frame(data=[go.Contour(z=Z_t[:,:,it], colorscale='jet', showscale=True,zmin=zmin, zmax=zmax)]))

    # Agregar el último cuadro al inicio para que la animación se repita

    # Definir los fotogramas de la animación
    fig.frames = frames
    # el primero

    # Configurar el diseño de la figura y la animación
    fig.update_layout(
        title=title,
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(label='Play', method='animate', args=[None, {'frame': {'duration': duration, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}])],
            showactive=False,
        )],
    )
    # colorbar 


    # Mostrar la figura
    return fig 