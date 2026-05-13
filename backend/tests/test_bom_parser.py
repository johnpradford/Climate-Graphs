from backend.acquisition.bom_parsers import BOMClimateParser


def test_parse_simple_table():
    html = '''
    <table>
        <tr>
            <th>Month</th>
            <th>Rainfall</th>
        </tr>
        <tr>
            <td>Jan</td>
            <td>25.4</td>
        </tr>
    </table>
    '''

    parser = BOMClimateParser()

    dataframe = parser.parse_climate_table(html)

    assert dataframe.iloc[0]['Month'] == 'Jan'
