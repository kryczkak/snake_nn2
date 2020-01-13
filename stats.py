from numpy import sign
class Stats():

    def __init__(self,
                 snak_pos_x, snak_pos_y,
                 snake_head_pos_x, snake_head_pos_y,
                 output_direction_x, output_direction_y,
                 snake_body, num_rows, direction):

        self.score = 0
        self.best_score = 0
        self.incremental = 1

        self.num_rows = num_rows

        self.snak_pos_x = snak_pos_x
        self.snak_pos_y = snak_pos_y
        self.snake_head_pos_x = snake_head_pos_x
        self.snake_head_pos_y = snake_head_pos_y

        self.snak_distance_x = sign(snak_pos_x - snake_head_pos_x)
        self.snak_distance_y = sign(snak_pos_y - snake_head_pos_y)

        self.tail_distance_x = 0
        self.tail_distance_y = 0

        self.distance_r = 0
        self.distance_l = 0
        self.distance_u = 0
        self.distance_d = 0

        self.categorical_direction = 'r'

        self.count_distanses(snake_body, num_rows, direction)


    def reset_score(self):
        self.score = 0


    def increase_score(self):
        self.score += self.incremental
        if self.score > self.best_score:
            self.best_score = self.score


    def count_distanses(self, snake_body, num_rows, direction):
        head = snake_body[-1]
        if len(snake_body)>1:
            neck = snake_body[-2]
        else:
            neck = snake_body[-1]

        if direction == 'r':
            if head[0] + 1 == neck[0]:
                distance = 0
            else:
                distance = num_rows - head[0] - 1
                for peace in snake_body:
                    if head[1] == peace[1] and head[0] < peace[0]:
                        peace_num = snake_body.index(peace)
                        peace_distance = peace[0] - head[0] - 1
                        if distance > peace_distance and peace_distance < peace_num:
                            distance = peace_distance

        elif direction == 'l':
            if head[0] - 1 == neck[0]:
                distance = 0
            else:
                distance = head[0]
                for peace in snake_body:
                    if head[1] == peace[1] and head[0] > peace[0]:
                        peace_num = snake_body.index(peace)
                        peace_distance = head[0] - peace[0] - 1
                        if distance > peace_distance and peace_distance < peace_num:
                            distance = peace_distance

        elif direction == 'u':
            if head[1] - 1 == neck[1]:
                distance = 0
            else:
                distance = head[1]
                for peace in snake_body:
                    if head[0] == peace[0] and head[1] > peace[1]:
                        peace_num = snake_body.index(peace)
                        peace_distance = head[1] - peace[1] - 1
                        if distance > peace_distance and peace_distance < peace_num:
                            distance = peace_distance

        elif direction == 'd':
            if head[1] + 1 == neck[1]:
                distance = 0
            else:
                distance = num_rows - head[1] - 1
                for peace in snake_body:
                    if head[0] == peace[0] and head[1] < peace[1]:
                        peace_num = snake_body.index(peace)
                        peace_distance =  peace[1] - head[1] - 1
                        if distance > peace_distance and peace_distance < peace_num:
                            distance = peace_distance

        if distance > 1:
            distance = 1
        elif distance ==  1:
            distance = 1
        else:
            distance = -1
        count_distanses = distance
        return count_distanses


    def set_stats(self,
                 snak_pos_x, snak_pos_y,
                 snake_head_pos_x, snake_head_pos_y,
                 snake_body, num_rows):

        tail = snake_body[0]

        self.snak_distance_x = sign(snak_pos_x - snake_head_pos_x)
        self.snak_distance_y = sign(snak_pos_y - snake_head_pos_y)

        self.tail_distance_x = (tail[0] - snake_head_pos_y) / self.num_rows
        self.tail_distance_y = (tail[1] - snake_head_pos_y) / self.num_rows


        self.distance_r = self.count_distanses(snake_body, num_rows, 'r')
        self.distance_l = self.count_distanses(snake_body, num_rows, 'l')
        self.distance_u = self.count_distanses(snake_body, num_rows, 'u')
        self.distance_d = self.count_distanses(snake_body, num_rows, 'd')



    def set_dir(self, dir_x, dir_y):
        if dir_x == 1:
            self.categorical_direction = 0 #'r'
        elif dir_x == -1:
            self.categorical_direction = 1 #'l'
        elif dir_y == -1:
            self.categorical_direction = 2 # 'u'
        elif dir_y == 1:
            self.categorical_direction = 3 # 'd'



    def save_stats_to_file(self, file_name):
        file_object = open(file_name, 'a')
        file_object.writelines(
                str(self.snak_distance_x) + ',' +
                str(self.snak_distance_y) + ',' +
                str(self.distance_r)  + ',' +
                str(self.distance_l) + ',' +
                str(self.distance_u) + ',' +
                str(self.distance_d) + ',' +
                #str(self.tail_distance_x) + ',' +
                #str(self.tail_distance_x) + ',' +
                str(self.categorical_direction)  + '\n'
        )
        file_object.close()



