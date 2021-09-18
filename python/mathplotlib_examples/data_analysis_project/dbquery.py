dailyUserCountByPurchaseAmt = {
    '2017_06_11':  "select round(daily_rev), count(*) from aggregates.user_retention_daily where stat_date = '2017-06-11' and daily_rev > 0 group by 1 order by 1 limit 10000"
}

instalCountByZip = {
    'No. of. Installs by Zipcode' : "SELECT eventvalue02 AS zipcode, COUNT(1) FROM raw_events_authenticated_current WHERE ingest_time >= '2017-06-12 00:00:00' and ingest_time < '2017-06-13 00:00:00' AND   event_type = 3332 AND   eventvalue01 = 'INSTALL' AND   eventvalue05 = 'US' GROUP BY 1 ORDER BY 1 DESC LIMIT 30000"
}

zipcodeWiseMeanSpending = {
    "Zip code wise mean spending (only zipcode with 50 or more players)" : "select zipcode, players, round(totrev/players) from ( SELECT zipcode, COUNT(1) as players, sum(rev) as totrev FROM temptest.player_zipcode a JOIN (SELECT player_id, max(ltd_gross_rev) as rev FROM aggregates.mtx_transactions WHERE game_server_timestamp >= '2017-01-01' group by 1) b ON a.player_id = b.player_id GROUP BY 1) where players >= 50 and zipcode <> 'null' order by 2 desc"
}
zipcodeWiseSpenders = {
    "zip code wise spenders since 2017-01-01" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01') b on a.player_id = b.player_id group by 1"
}

zipcodeWiseSpendersAbove1000 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev >= 1000) b on a.player_id = b.player_id group by 1 order by 2 desc"
}

zipcodeWiseSpendersBelow100 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev <= 100) b on a.player_id = b.player_id group by 1 order by 2 desc"
}

zipcodeWiseSpendersAbove100Below500 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev > 100 and ltd_gross_rev < 500) b on a.player_id = b.player_id group by 1 order by 2 desc"
}

zipcodeWiseSpendersAbove5000 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev >  5000) b on a.player_id = b.player_id group by 1 order by 2 desc"
}
zipcodeWiseSpendersBelow20 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev <  20) b on a.player_id = b.player_id group by 1 order by 2 desc"
}
zipcodeWiseSpendersAbove10000 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and ltd_gross_rev >  10000) b on a.player_id = b.player_id group by 1 order by 2 desc"
}
zipcodeWiseSpendersDaysInGameMoreThan30 = {
    "zip code wise spenders since 2017-01-01 above 1000" : "select zipcode, count(1) from temptest.player_zipcode a join ( select distinct player_id from aggregates.mtx_transactions where game_server_timestamp >= '2017-01-01' and days_in_game >= 30) b on a.player_id = b.player_id group by 1 order by 2 desc"
}
cheatersSince2017 = {
    "cheatersSince2017" : "SELECT zipcode, COUNT(1) FROM temptest.player_zipcode a JOIN (SELECT DISTINCT player_id FROM temptest.cheaters ) b ON trim(a.player_id) = trim(b.player_id) GROUP BY 1 ORDER BY 2 DESC"
}

cheatersSince2017WorldWide = {
    "cheatersSince2017WorldWide" : "SELECT country_code, COUNT(1) FROM temptest.player_country a JOIN (SELECT DISTINCT player_id FROM temptest.cheaters) b ON TRIM (a.player_id) = TRIM (b.player_id) where country_code != '' GROUP BY 1 ORDER BY 2 DESC"
}

listOfChurnPlayers = {
    "listOfChurnPlayers" : "select time_played_secs, num_sessions from temptest.churn_player where num_sessions < 40 and time_played_secs < 4000 "
}

listOfNotChurnPlayers = {
    "listOfNotChurnPlayers" : "select time_played_secs, num_sessions from temptest.not_churn_player where num_sessions < 40 and time_played_secs < 4000 "
}

activeInactivePlayerStats = {
    "inactive_avg_played" : "select install_date, avg_time_played_in_mins from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_avg_played" : "select install_date, avg_time_played_in_mins from aggregates.active_inactive_player_stats where players_status = 'active' order by 1",
    "inactive_median_played" : "select install_date, median_time_played_in_mins from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_median_played" : "select install_date, median_time_played_in_mins from aggregates.active_inactive_player_stats where players_status = 'active' order by 1"
}

activeInactivePlayerLevel = {
    "inactive_avg_lvl" : "select install_date, avg_level from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_avg_lvl" : "select install_date, avg_level from aggregates.active_inactive_player_stats where players_status = 'active' order by 1",
    "inactive_mid_lvl" : "select install_date, median_level from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_mid_lvl" : "select install_date, median_level from aggregates.active_inactive_player_stats where players_status = 'active' order by 1"
}

activeInactivePlayerSessions = {
    "inactive_avg_session" : "select install_date, avg_sessions from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_avg_session" : "select install_date, avg_sessions from aggregates.active_inactive_player_stats where players_status = 'active' order by 1",
    "inactive_mid_session" : "select install_date, median_sessions from aggregates.active_inactive_player_stats where players_status = 'inactive' order by 1",
    "active_mid_session" : "select install_date, median_sessions from aggregates.active_inactive_player_stats where players_status = 'active' order by 1"
}
