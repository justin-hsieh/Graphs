import random

class Queue:
    def __init__(self):
        self.storage = []
    
    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(i + 1)

        # generate possible friendship combinations
        friendship_combos = []

        # for user in user dict
        for user_id in self.users:
            # ensures all combos accounted for 
            for friend_id in range(user_id + 1, self.last_id + 1):
                # append friendship combo 
                friendship_combos.append((user_id, friend_id))

        # randomly shuffle the friendship combos
        random.shuffle(friendship_combos)

        for i in range(0, (num_users * avg_friendships // 2)):
            # assign friendship based on index
            friendship = friendship_combos[i]
            # add friendship
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        # initiate queue
        q = Queue()
        # put user ID into queue
        q.enqueue([user_id])
        # while queue is not empty
        while q.size() > 0:
            # dequeue first item, initiate path
            path = q.dequeue()
            newUserID = path[-1]
            # if user ID has not been visited
            if newUserID not in visited:
                # add it to visited
                visited[newUserID] = path
                # for friend ID in friendships
                for friendID in self.friendships[newUserID]:
                    # if friend ID hasn't been visited
                    if friendID not in visited:
                        # copy path
                        new_path = list(path)
                        # append friend ID
                        new_path.append(friendID)
                        # add path to queue to keep updating it
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
