import React from 'react';
import MUIDataTable from "mui-datatables";

const MonitorTable = ({ data }) => {
    const columns = [
        {
            name: "latitude",
            label: "Latitud",
            options: {
                filter: true,
                sort: true,
                viewColumns: true
            }
        },
        {
            name: "longitude",
            label: "Longitud",
            options: {
                filter: true,
                sort: true,
                viewColumns: true
            }
        },
        {
            name: "temperature",
            label: "Temperatura",
            options: {
                filter: true,
                sort: true,
                viewColumns: true
            }
        },
        {
            name: "time",
            lable: "Tiempo",
            options: {
                filter: true,
                sort: true,
                viewColumns: true
            }
        }
    ];

    const info = Object.keys( data ).map(( key ) => {
        return {
            latitude: data[key].latitude,
            longitude: data[key].longitude,
            temperature: data[key].temperature,
            time: data[key].time
        }
    });

    const options = {
        filter: true,
        selectableRows: 'none',
        responsive: "scrollMaxHeight",
        fixedHeaderOptions: {
            xAxis: true,
            yAxis: true
        },
        textLabels: {
            body: {
                noMatch: "Lo sentimos, no se encontraron registros coincidentes",
                toolTip: "Ordenar",
                columnHeaderTooltip: column => `Ordenar por ${column.label}`
            },
            pagination: {
                next: "Sig. Pag.",
                previous: "Ant. Pag",
                rowsPerPage: "Filas por pag.:",
                displayRows: "de",
            },
            toolbar: {
                search: "Buscar",
                downloadCsv: "Descargar CSV",
                print: "Imprimir",
                viewColumns: "Columnas",
                filterTable: "Filtrar Tabla",
            },
            filter: {
                all: "Todos",
                title: "FILTROS",
                reset: "REINICIAR",
            },
            viewColumns: {
                title: "Mostar Columnas",
                titleAria: "Mostar/Ocultar Columnas",
            },
            selectedRows: {
                text: "Fila(s) seleccionadas",
                delete: "Eliminar",
                deleteAria: "Eliminar Filas Seleccionadas",
            },
        },
        filterType: 'multiselect',
        print: false,
        download: false
    }

    return (
        <div id="monitorTable">
            <MUIDataTable
                title="RaspBerryPi"
                data = { info }
                columns = { columns }
                options = { options }
            />
        </div>
    )
}
export default MonitorTable;