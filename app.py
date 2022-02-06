# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import folium
import gspread

sa = gspread.service_account(filename="roadsignpost-b2c17aec850b.json")
sh = sa.open("Test Copy RSP")

wks = sh.worksheet("Form responses 1")
#sheet = sh.worksheet("Form responses 3")

app = Flask(__name__)
cond = wks.col_values(2)
lat = wks.col_values(3)
lon = wks.col_values(4)


@app.route('/')
def base():
    # this is base map
    map = folium.Map(
        location=[-12.77596, 28.19201]
    )
    #address = wks.col_values(5)
    for i in range(0, len(lat)):
        #cad = [cond[i], lat[i], lon[i]]
        try:
            folium.Marker(
                location=[lat[i], lon[i]],
                popup=cond[i],
                tooltip="Click Here!"
            ).add_to(map)
        except:
            pass
    return map._repr_html_()


@app.route("/open-street-map")
def open_street_map():
    # this map using stamen toner
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Toner',
        zoom_start=13
    )

    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)

    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
