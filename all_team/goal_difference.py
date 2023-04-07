from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

html = '''
<tbody class="standingEntriesContainer isPL"><tr class="tableDark" data-filtered-table-row="26" data-filtered-table-row-name="Arsenal" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">1</span> <span class="movement none"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/1/Arsenal/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t3.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t3.png, https://resources.premierleague.com/premierleague/badges/20/t3@x2.png 2x"> </span> Arsenal </a> </td> <td>29</td> <td>+43 </td> <td class="points">72</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Man City" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">2</span> <span class="movement none"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/11/Manchester-City/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t43.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t43.png, https://resources.premierleague.com/premierleague/badges/20/t43@x2.png 2x"> </span> Man City </a> </td> <td>28</td> <td>+45 </td> <td class="points">64</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Newcastle" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">3</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/23/Newcastle-United/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t4.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t4.png, https://resources.premierleague.com/premierleague/badges/20/t4@x2.png 2x"> </span> Newcastle </a> </td> <td>28</td> <td>+26 </td> <td class="points">53</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Man Utd" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">4</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/12/Manchester-United/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t1.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t1.png, https://resources.premierleague.com/premierleague/badges/20/t1@x2.png 2x"> </span> Man Utd </a> </td> <td>28</td> <td>+5 </td> <td class="points">53</td> </tr> <tr class="tableLight" data-filtered-table-row="26" data-filtered-table-row-name="Spurs" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">5</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/21/Tottenham-Hotspur/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t6.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t6.png, https://resources.premierleague.com/premierleague/badges/20/t6@x2.png 2x"> </span> Spurs </a> </td> <td>29</td> <td>+12 </td> <td class="points">50</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Brighton" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">6</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/131/Brighton-and-Hove-Albion/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t36.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t36.png, https://resources.premierleague.com/premierleague/badges/20/t36@x2.png 2x"> </span> Brighton </a> </td> <td>27</td> <td>+17 </td> <td class="points">46</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Aston Villa" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">7</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/2/Aston-Villa/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t7.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t7.png, https://resources.premierleague.com/premierleague/badges/20/t7@x2.png 2x"> </span> Aston Villa </a> </td> <td>29</td> <td>-1 </td> <td class="points">44</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Liverpool" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">8</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/10/Liverpool/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t14.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t14.png, https://resources.premierleague.com/premierleague/badges/20/t14@x2.png 2x"> </span> Liverpool </a> </td> <td>28</td> <td>+15 </td> <td class="points">43</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Brentford" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">9</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/130/Brentford/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t94.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t94.png, https://resources.premierleague.com/premierleague/badges/20/t94@x2.png 2x"> </span> Brentford </a> </td> <td>29</td> <td>+8 </td> <td class="points">43</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Fulham" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">10</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/34/Fulham/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t54.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t54.png, https://resources.premierleague.com/premierleague/badges/20/t54@x2.png 2x"> </span> Fulham </a> </td> <td>28</td> <td>0 </td> <td class="points">39</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Chelsea" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">11</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/4/Chelsea/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t8.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t8.png, https://resources.premierleague.com/premierleague/badges/20/t8@x2.png 2x"> </span> Chelsea </a> </td> <td>29</td> <td>-1 </td> <td class="points">39</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Crystal Palace" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">12</span> <span class="movement none"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/6/Crystal-Palace/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t31.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t31.png, https://resources.premierleague.com/premierleague/badges/20/t31@x2.png 2x"> </span> Crystal Palace </a> </td> <td>29</td> <td>-15 </td> <td class="points">30</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Leeds" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">13</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/9/Leeds-United/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t2.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t2.png, https://resources.premierleague.com/premierleague/badges/20/t2@x2.png 2x"> </span> Leeds </a> </td> <td>29</td> <td>-11 </td> <td class="points">29</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Wolves" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">14</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/38/Wolverhampton-Wanderers/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t39.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t39.png, https://resources.premierleague.com/premierleague/badges/20/t39@x2.png 2x"> </span> Wolves </a> </td> <td>29</td> <td>-19 </td> <td class="points">28</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="West Ham" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">15</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/25/West-Ham-United/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t21.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t21.png, https://resources.premierleague.com/premierleague/badges/20/t21@x2.png 2x"> </span> West Ham </a> </td> <td>28</td> <td>-13 </td> <td class="points">27</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Everton" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">16</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/7/Everton/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t11.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t11.png, https://resources.premierleague.com/premierleague/badges/20/t11@x2.png 2x"> </span> Everton </a> </td> <td>29</td> <td>-18 </td> <td class="points">27</td> </tr> <tr class="" data-filtered-table-row="26" data-filtered-table-row-name="Nott'm Forest" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">17</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/15/Nottingham-Forest/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t17.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t17.png, https://resources.premierleague.com/premierleague/badges/20/t17@x2.png 2x"> </span> Nott'm Forest </a> </td> <td>29</td> <td>-28 </td> <td class="points">27</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Bournemouth" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">18</span> <span class="movement up"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/127/Bournemouth/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t91.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t91.png, https://resources.premierleague.com/premierleague/badges/20/t91@x2.png 2x"> </span> Bournemouth </a> </td> <td>29</td> <td>-30 </td> <td class="points">27</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Leicester" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">19</span> <span class="movement down"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/26/Leicester-City/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t13.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t13.png, https://resources.premierleague.com/premierleague/badges/20/t13@x2.png 2x"> </span> Leicester </a> </td> <td>29</td> <td>-11 </td> <td class="points">25</td> </tr> <tr class="tableMid" data-filtered-table-row="26" data-filtered-table-row-name="Southampton" data-filtered-table-row-abbr="26"> <td class="pos"> <span class="value">20</span> <span class="movement none"></span> </td> <td class="team" scope="row"> <a href="//www.premierleague.com/clubs/20/Southampton/overview"> <span class="badge badge-image-container" data-widget="club-badge-image" data-size="20"> <img class="badge-image badge-image--20 js-badge-image" src="https://resources.premierleague.com/premierleague/badges/20/t20.png" srcset="https://resources.premierleague.com/premierleague/badges/20/t20.png, https://resources.premierleague.com/premierleague/badges/20/t20@x2.png 2x"> </span> Southampton </a> </td> <td>29</td> <td>-24 </td> <td class="points">23</td> </tr> </tbody>
'''

soup = BeautifulSoup(html, 'html.parser')
teams = soup.find_all('tr')

team_names = []
goal_differences = []

for team in teams:
    team_name = team.find('td', class_='team').text.strip()
    goal_difference = int(team.find_all('td')[3].text.strip())
    team_names.append(team_name)
    goal_differences.append(goal_difference)

plt.bar(team_names, goal_differences)
plt.xlabel('Team Names')
plt.ylabel('Goal Difference')
plt.xticks(rotation=90)
plt.title('Goal Difference by Team')
plt.tight_layout()
plt.savefig('goal_differences.png', dpi=300)
plt.show()