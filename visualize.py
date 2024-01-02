import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = ''
database = 'jojo'
host = 'localhost'
port = '5433'

view1 = '''
CREATE OR REPLACE VIEW view_query1 AS
SELECT DISTINCT user_name, stand_name, stand.pwr AS stand_power
FROM stand_user
JOIN stand ON stand_user.id_stand = stand.id_stand
WHERE stand.pwr LIKE 'A'
'''


view2 = '''
CREATE OR REPLACE VIEW view_query2 AS
SELECT user_name, part_num AS stand_power
FROM stand_user
JOIN part ON stand_user.id_part = part.id_part
WHERE part.part_num = 5
'''

view3 = '''
CREATE OR REPLACE VIEW view_query3 AS
SELECT stand_name, dev
FROM stand
ORDER BY
    CASE
        WHEN dev = 'Infi' THEN 1
        WHEN dev = 'A' THEN 2
        WHEN dev = 'B' THEN 3
        WHEN dev = 'C' THEN 4
        WHEN dev = 'D' THEN 5
        WHEN dev = 'E' THEN 6
    END DESC
'''

def visualize(result_1, result_2, result_3):
    # Sort only the first plot
    result_1.sort(key=lambda x: x[0])

    total = []
    att = []
    for row in result_1:
        att.append(row[0])
        total.append(row[1])

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    figure.set_size_inches(18, 10, forward=True)

    # Bar Plot
    bar = bar_ax.bar(range(len(att)), total, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(range(len(att)))  # Set ticks for all items
    bar_ax.set_xticklabels(att, rotation=45, ha='right')  # Manually set x-axis labels with rotation
    bar_ax.set_xlabel('Користувачі')
    bar_ax.set_ylabel('Станд')
    bar_ax.set_title('Відповідність між Користувачем та Стандом із силою А')

    # Pie Chart
    total = []
    labels = []
    for row in result_2:
        labels.append(row[0])
        total.append(row[1])

    pie_ax.pie(total, labels=labels, autopct='%1.1f%%')
    pie_ax.set_title('Користувачі з 5 сезону')

    # Line Plot
    att = []
    quan = []

    for row in result_3:
        att.append(row[0])
        quan.append(row[1])

    # Plot without x-axis labels
    graph_ax.plot(range(len(att)), quan, marker='o')
    graph_ax.set_xticks([])  # Remove x-axis ticks
    graph_ax.set_xlabel('Станди')
    graph_ax.set_ylabel('Рівень')
    graph_ax.set_title('Графік залежності станду від рівня його розвитку(dev)')

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn.cursor() as cur:
    cur.execute(view1)
    cur.execute(view2)
    cur.execute(view3)

    cur.execute("select * from view_query1")
    result_1 = cur.fetchall()
    cur.execute("select * from view_query2")
    result_2 = cur.fetchall()
    cur.execute("select * from view_query3")
    result_3 = cur.fetchall()
    visualize(result_1, result_2, result_3)
