import pymysql
import config
import time

db_args = {
    "host": config.mysql["host"],
    "port": config.mysql["port"],
    "user": config.mysql["user"],
    "password": config.mysql["pass"],
    "database": config.mysql["db"],
    "charset": 'utf8mb4',
    "cursorclass": pymysql.cursors.DictCursor
}

def get_date_time():
    return time.strftime("%d/%m/%Y - %H:%M:%S")

def setup_database():
    db = pymysql.connect(**db_args)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `configs` (`id` INT NOT NULL AUTO_INCREMENT, `guild_id` BIGINT, `prefix` VARCHAR(5), PRIMARY KEY (`id`));")
    cursor.execute("CREATE TABLE IF NOT EXISTS `leveling` (`id` INT NOT NULL AUTO_INCREMENT, `guild_id` BIGINT, `user_id` BIGINT, `xp` BIGINT, `level` INT, PRIMARY KEY (`id`));")
    db.commit()
    cursor.close()
    db.close()
    print("> Initialized MySQL database.")

def get_config(guild_id):
    db = pymysql.connect(**db_args)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `configs` WHERE guild_id = '%s';", (guild_id))
    conf = cursor.fetchall()
    if len(conf) > 0:
        cursor.close()
        db.close()
        return conf[0]
    else:
        print(f"> [{get_date_time()}] {guild_id}'s config has been created.")
        cursor.execute("INSERT INTO `configs` VALUES (0, %s, '.');", (guild_id))
        conf = {'id': db.insert_id(), 'guild_id': guild_id, 'prefix': '.'}
        db.commit()
        cursor.close()
        db.close()
        return conf

def change_config(guild_id, item, value):
    try:
        db = pymysql.connect(**db_args)
        cursor = db.cursor()
        cursor.execute(f"UPDATE configs SET `{item}` = %s WHERE guild_id = %s;", (value, guild_id))
        print(f"> [{get_date_time()}] Changed '{item}' for guild '{guild_id}' to '{value}'.")
        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        return False

def get_user_xp(guild_id, user_id):
    db = pymysql.connect(**db_args)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM `leveling` WHERE `guild_id` = {guild_id} AND user_id = {user_id}")
    result = cursor.fetchall()
    if len(result) > 0:
        cursor.close()
        db.close()
        return result[0]
    else:
        cursor.execute(f"INSERT INTO `leveling` VALUES (0, {guild_id}, {user_id}, 0, 0)")
        db.commit()
        user_xp = {"id": db.insert_id(), "guild_id": guild_id, "user_id": user_id, "xp": 0, "level": 0}
        cursor.close()
        db.close()
        print(f"> [{get_date_time()}] Leveling: Created user {user_id} in guild {guild_id}.")
        return user_xp

def add_user_xp(guild_id, user_id, xp_to_add):
    db = pymysql.connect(**db_args)
    current_xp = get_user_xp(guild_id, user_id)["xp"]
    updated_xp = current_xp + xp_to_add

    cursor = db.cursor()
    cursor.execute(f"UPDATE `leveling` SET `xp` = {updated_xp} WHERE `guild_id` = {guild_id} AND`user_id` = {user_id}")
    db.commit()
    cursor.close()
    db.close()

    print(f"> [{get_date_time()}] Leveling: User {user_id} in guild {guild_id} earned {xp_to_add} XP.")
    return updated_xp

def get_user_level(guild_id, user_id):
    db = pymysql.connect(**db_args)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM `leveling` WHERE `guild_id` = {guild_id} AND`user_id` = {user_id}")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    if len(result) > 0:
        return result[0]["level"]
    else:
        return False

def user_level_up(guild_id, user_id):
    db = pymysql.connect(**db_args)
    cursor = db.cursor()
    cursor.execute(f"UPDATE `leveling` SET `level` = `level` + 1")
    db.commit()
    cursor.close()
    db.close()
    return True

