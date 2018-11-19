import datetime

class Users:
    
    users = []
    loggedInUsers = []

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.lastLoggedInAt = None


    def create_user(self):
        if len(Users.users) == 0:
            user_id = 1
        else:
            user_id = len(Users.users)+1
        newUser = {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "lastLoggedInAt": self.lastLoggedInAt,
            "user_id": user_id
        }
        Users.users.append(newUser)
        print(newUser)

    @staticmethod
    def login(username, password):
        for current_user in Users.users:
            if current_user["username"] == username and current_user["password"] == password:
                current_user["lastLoggedInAt"] = datetime.datetime.utcnow()
                Users.loggedInUsers.append(current_user["user_id"])
                print("Logged in successfully")

    @staticmethod
    def logout():
        Users.loggedInUsers.pop()


class Comments:
    
    comments = []

    def __init__(self, message):
        self.timestamp = datetime.datetime.utcnow()
        self.message = message

    def make_comment(self):
        user_id = Users.loggedInUsers[0]
        for current_user in Users.users:
            if current_user["user_id"] == user_id:
                author = current_user["username"]

        if len(Comments.comments) == 0:
            comment_id = 1
        else:
            comment_id = len(Comments.comments)+1

        new_comment = {
            "message": self.message,
            "author": author,
            "timestamp": self.timestamp,
            "comment_id": comment_id
        }
        Comments.comments.append(new_comment)
    
    def delete_comment(self, comment_id):
        user_id = Users.loggedInUsers[0]
        for current_user in Users.users:
            if current_user["role"] == "admin" or current_user["role"]=="moderator":
                author = current_user["username"]

        # for comment in Comments.comments:
        #     if comment["comment_id"] == comment_id
        if comment_id<=len(Comments.comments) and comment_id>0:
            Comments.comments.pop(comment_id-1)
        else: 
            print('Comment does not exist')

    def edit_comment(self, message, comment_id):
        if comment_id<=len(Comments.comments) and comment_id>0:
            if Users.users[Users.loggedInUsers[0]-1]["username"] == Comments.comments[comment_id-1]['author']:
                Comments.comments[comment_id-1]['message']= message


user = Users('Boli', '12345678', 'user')
user.create_user()

print(Users.users)
user.login('Boli','12345678')
comment = Comments('What is github?')
comment.make_comment()
print(Comments.comments)
comment.edit_comment('Me no understand this', 1)
print(Comments.comments)




