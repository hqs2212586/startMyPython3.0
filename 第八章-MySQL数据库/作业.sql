-- 1、自行创建测试数据；
create database db5;
use db5;

create table teacher (
    tid int primary key auto_increment,
    tname char(20) not null
);

insert into teacher(tname) values
    ('张三'),
    ('李四'),
    ('王五'),
    ('赵六'),
    ('马七');

create table class_grade (
    gid int primary key auto_increment,
    gname char(20) not null
);

insert into class_grade(gname) values
    ('一年级'),
    ('二年级'),
    ('三年级'),
    ('四年级'),
    ('五年级');

create table course (
    cid int primary key auto_increment,
    cname char(20) not null,
    teacher_id int,
    foreign key(teacher_id) references teacher(tid)
    on delete cascade
    on update cascade
);

insert into course(cname, teacher_id) values
    ('生物',1),
    ('体育',1),
    ('物理',2),
    ('语文',3),
    ('数学',4),
    ('外语',5);

create table class (
    cid int primary key auto_increment,
    caption char(20),
    grade_id int,
    foreign key(grade_id) references class_grade(gid)
    on delete cascade
    on update cascade
);

insert into class(caption, grade_id) values
    ('一年一班',1),
    ('一年二班',1),
    ('二年一班',2),
    ('二年二班',2),
    ('三年一班',3),
    ('四年一班',4),
    ('五年一班',5);

create table student (
    sid int primary key auto_increment,
    sname char(20),
    gender enum('男', '女') not null,
    class_id int,
    foreign key(class_id) references class(cid)
    on delete cascade
    on update cascade
);

insert into student(sname,gender,class_id) values
    ('乔丹','女',1),
    ('艾弗森','女',1),
    ('科比','男',2),
    ('curry','男',2),
    ('james','男',3),
    ('李瑞','女',4),
    ('白雪','女',5),
    ('无敌','男',5),
    ('天剑','男',6),
    ('egon','女',7),
    ('alex','男',7);

create table score (
    sid int primary key auto_increment,
    student_id int,
    course_id int,
    score int,
    foreign key(student_id) references student(sid)
    on delete cascade
    on update cascade,
    foreign key(course_id) references course(cid)
    on delete cascade
    on update cascade
);

insert into score(student_id, course_id, score) values
    (1,1,60),
    (1,2,59),
    (1,3,58),
    (1,4,71),
    (1,5,68),
    (1,6,100),
    (2,1,90),
    (2,2,99),
    (2,3,71),
    (2,4,68),
    (2,5,92),
    (2,6,88),
    (3,1,23),
    (3,2,55),
    (3,3,72),
    (3,4,88),
    (3,5,92),
    (3,6,12),
    (4,2,65),
    (4,4,78),
    (4,5,34),
    (5,2,75),
    (5,4,38),
    (5,5,44),
    (6,2,23),
    (6,4,32),
    (6,5,0),
    (7,1,78),
    (7,3,60),
    (7,6,45),
    (8,1,43),
    (8,3,65),
    (8,6,99),
    (9,2,56),
    (9,3,69),
    (9,5,78),
    (10,2,43),
    (10,3,69),
    (10,5,90),
    (11,2,90),
    (11,3,89),
    (11,5,100);

create table teach2cls (
    tcid int primary key auto_increment,
    tid int,
    cid int,
    foreign key(tid) references teacher(tid)
    on delete cascade
    on update cascade,
    foreign key(cid) references class(cid)
    on delete cascade
    on update cascade
);

insert into teach2cls(tid, cid) values     # 五个老师、七个班级
    (1,1),
    (1,2),
    (1,5),
    (1,7),
    (2,2),
    (2,3),
    (2,4),
    (2,6),
    (3,1),
    (3,2),
    (3,4),
    (3,5),
    (3,6),
    (4,2),
    (4,4),
    (4,7),
    (5,5),
    (5,6),
    (5,7);



-- 2、查询学生总人数；
select count(sid) as total_num from student;
+-----------+
| total_num |
+-----------+
|        11 |
+-----------+

-- 3、查询“生物”课程和“物理”课程成绩都及格的学生id和姓名；
select sid, sname from student where sid in (
    select
        score.student_id    # 先找到学习了这两们课且都及格学生的id
    from
        score
    inner join course
        on score.course_id=course.cid
    where
        course.cname in (
            '生物',
            '物理'
        )
        and score.score >=60
    group by
        score.student_id
    having
        count(course_id) =2
);
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾弗森    |
|   7 | 白雪      |
+-----+-----------+

-- 4、查询每个年级的班级数，取出班级数最多的前三个年级；
select
    gname,count(class.cid)
from
    class_grade
inner join
    class
on class.grade_id=class_grade.gid
group by gid
order by count(cid) DESC
limit 3;
+-----------+------------------+
| gname     | count(class.cid) |
+-----------+------------------+
| 一年级    |                2 |
| 二年级    |                2 |
| 四年级    |                1 |
+-----------+------------------+

-- 5、查询平均成绩最高和最低的学生的id和姓名以及平均成绩；
select * from (
select
    avg(score) as avg_score
from
    score
group by
    student_id
order by avg_score ASC
limit 1 ) t1 union
select * from
(select
    avg(score) as avg_score
from
    score
group by
    student_id
order by avg_score DESC
limit 1) t2;
+-----------+
| avg_score |
+-----------+
|   18.3333 |
|   93.0000 |
+-----------+
select
    student_id,
    concat(student.sname) as student_name,
    avg(score)
from
    student
inner join
    score
on score.student_id=student.sid
group by
    student_id
having
    avg(score) in (
        select * from (
            select
                avg(score) as avg_score
            from
                score
            group by
                student_id
            order by avg_score ASC
            limit 1 ) t1
        union
        select * from(
            select
                avg(score) as avg_score
            from
                score
            group by
                student_id
            order by avg_score DESC
            limit 1) t2
    );
# 由于最小成绩是无限小数，无法显示
+------------+--------------+------------+
| student_id | student_name | avg(score) |
+------------+--------------+------------+
|         11 | alex         |    93.0000 |
+------------+--------------+------------+

-- 6、查询每个年级的学生人数；
select
    grade_id, count(sid)
from
    student
left join
    class
on student.class_id=class.cid
group by
    grade_id;
+----------+------------+
| grade_id | count(sid) |
+----------+------------+
|        1 |          4 |
|        2 |          2 |
|        3 |          2 |
|        4 |          1 |
|        5 |          2 |
+----------+------------+
select
    gname, t1.stu_num as stu_num
from
    class_grade
inner join
    (select
        grade_id, count(sid) as stu_num
    from
        student
    left join
        class
    on student.class_id=class.cid
    group by
        grade_id) as t1
on class_grade.gid=t1.grade_id;
+-----------+---------+
| gname     | stu_num |
+-----------+---------+
| 一年级    |       4 |
| 二年级    |       2 |
| 三年级    |       2 |
| 四年级    |       1 |
| 五年级    |       2 |
+-----------+---------+

-- 7、查询每位学生的学号，姓名，选课数，平均成绩；
select
    student.sid,
    concat(student.sname),
    count(course_id) as course_num,
    avg(score) as avg_score
from
    student
inner join
    score
on student.sid=score.student_id
group by student.sid;
+-----+-----------------------+------------+-----------+
| sid | concat(student.sname) | course_num | avg_score |
+-----+-----------------------+------------+-----------+
|   1 | 乔丹                  |          6 |   69.3333 |
|   2 | 艾弗森                |          6 |   84.6667 |
|   3 | 科比                  |          6 |   57.0000 |
|   4 | curry                 |          3 |   59.0000 |
|   5 | james                 |          3 |   52.3333 |
|   6 | 李瑞                  |          3 |   18.3333 |
|   7 | 白雪                  |          3 |   61.0000 |
|   8 | 无敌                  |          3 |   69.0000 |
|   9 | 天剑                  |          3 |   67.6667 |
|  10 | egon                  |          3 |   67.3333 |
|  11 | alex                  |          3 |   93.0000 |
+-----+-----------------------+------------+-----------+

-- 8、查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名、成绩最低的课程名及分数；
# score——》student——》course
select
    student.sname,
    course.cname,
    score.score
from
    score
left join student on score.student_id=student.sid
left join course on score.course_id=course.cid
where student.sid=2
and score in (
    select * from (
        select
            max(score)
        from
            score
        where
            student_id=2) t1
    union
    select * from (
        select
            min(score)
        from
            score
        where
            student_id=2) t2
);
+-----------+--------+-------+
| sname     | cname  | score |
+-----------+--------+-------+
| 艾弗森    | 体育   |    99 |
| 艾弗森    | 语文   |    68 |
+-----------+--------+-------+

-- 9、查询姓“李”的老师的个数和所带班级数；
select
    concat(teacher.tname),
    count(distinct teacher.tid) as teacher_num,
    count(teach2cls.cid) as class_num
from
    teacher
inner join
    teach2cls
on teacher.tid=teach2cls.tid
where
    tname like '李%'
group by teacher.tid;
+-----------------------+-------------+-----------+
| concat(teacher.tname) | teacher_num | class_num |
+-----------------------+-------------+-----------+
| 李四                  |           1 |         4 |
+-----------------------+-------------+-----------+


-- 10、查询班级数小于5的年级id和年级名；
select
    gid,
    gname
from
    class_grade
where gid in (
    select
        grade_id
    from
        class
    group by
        grade_id
    having
        count(cid) < 5 )
;
+-----+-----------+
| gid | gname     |
+-----+-----------+
|   1 | 一年级    |
|   2 | 二年级    |
|   3 | 三年级    |
|   4 | 四年级    |
|   5 | 五年级    |
+-----+-----------+


-- 11、查询班级信息，包括班级id、班级名称、年级、年级级别(12为低年级，34为中年级，56为高年级)，示例结果如下；
# mysql中case when then else end的用法
select
    class.cid,
    class.caption,
    class_grade.gname,
    case   # 如果
        when class_grade.gid between 1 and 2 then '低年级'   # when后接条件，then后接返回值
        when class_grade.gid between 3 and 4 then '中年级'
        when class_grade.gid between 5 and 6 then '高年级'
        else 0      # 其他的返回值
        end as  '年级级别'   # end代表结束，自定义为'年级级别'
from
    class
inner join
    class_grade
on class.grade_id=class_grade.gid;
+-----+--------------+-----------+--------------+
| cid | caption      | gname     | 年级级别     |
+-----+--------------+-----------+--------------+
|   1 | 一年一班     | 一年级    | 低年级       |
|   2 | 一年二班     | 一年级    | 低年级       |
|   3 | 二年一班     | 二年级    | 低年级       |
|   4 | 二年二班     | 二年级    | 低年级       |
|   5 | 三年一班     | 三年级    | 中年级       |
|   6 | 四年一班     | 四年级    | 中年级       |
|   7 | 五年一班     | 五年级    | 高年级       |
+-----+--------------+-----------+--------------+

-- 12、查询学过“张三”老师2门课以上的同学的学号、姓名；
select
    sid,
    sname
from
    student
where
    sid in (
        select
            student_id
        from
            score
        where course_id in (
            select
                cid
            from
                course
            where
                teacher_id=(
                    select
                        tid
                    from
                        teacher
                    where
                        tname='张三'
                )
        )
        group by student_id
        having count(course_id)>=2
    );
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾弗森    |
|   3 | 科比      |
+-----+-----------+

-- 13、查询教授课程超过2门的老师的id和姓名；
select
    tid,
    tname
from
    teacher
where tid in (
    select
        teacher_id
    from
        course
    group by
        teacher_id
    having
        count(cid) >= 2
);
+-----+--------+
| tid | tname  |
+-----+--------+
|   1 | 张三   |
+-----+--------+

-- 14、查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        student_id
    from
        score
    where course_id in (1,2)
    group by
        student_id
);
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾弗森    |
|   3 | 科比      |
|   4 | curry     |
|   5 | james     |
|   6 | 李瑞      |
|   7 | 白雪      |
|   8 | 无敌      |
|   9 | 天剑      |
|  10 | egon      |
|  11 | alex      |
+-----+-----------+

-- 15、查询没有带过高年级的老师id和姓名；
select
    *
from
    teacher
where tid not in (
    select
        tid
    from
        teach2cls
    inner join
        class
    on teach2cls.cid=class.cid
    where class.grade_id in (5,6)
);
+-----+--------+
| tid | tname  |
+-----+--------+
|   2 | 李四   |
|   3 | 王五   |
+-----+--------+

-- 16、查询学过“张三”老师所教的所有课的同学的学号、姓名；
select
    sid,
    sname
from
    student
where class_id in (
    select
        cid    # 张三教过的班级id
    from
        teach2cls
    inner join
        teacher
    on teach2cls.tid=teacher.tid
    where teacher.tname='张三'
);
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾弗森    |
|   3 | 科比      |
|   4 | curry     |
|   7 | 白雪      |
|   8 | 无敌      |
|  10 | egon      |
|  11 | alex      |
+-----+-----------+

-- 17、查询带过超过2个班级的老师的id和姓名；
select
    *
from
    teacher
where tid in (
    select
        tid
    from
        teach2cls
    group by
        tid
    having
        count(cid) >= 2
);
+-----+--------+
| tid | tname  |
+-----+--------+
|   1 | 张三   |
|   2 | 李四   |
|   3 | 王五   |
|   4 | 赵六   |
|   5 | 马七   |
+-----+--------+

-- 18、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
select
    sid,
    sname
from
    student
where sid in(
    select
        t1.student_id
    from
        (select
            student_id,
            score as score_1
        from
            score
        where
            course_id=1) as t1
    inner join
        (select
            student_id,
            score as score_2
        from
            score
        where
            course_id=2) as t2
    on t1.student_id=t2.student_id
    where
        t2.score_2 > t1.score_1
);
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾弗森    |
|   3 | 科比      |
+-----+-----------+

-- 19、查询所带班级数最多的老师id和姓名；
select
    *
from
    teacher
where tid in (
    select
        tid     # 考虑带最多班级的是多个老师，老师的tid
    from
        teach2cls
    group by
        tid
    having
        count(cid)=(
            select          # 得到最多班级数量
                count(cid)
            from
                teach2cls
            group by
                tid
            order by
                count(cid) desc
            limit 1
        )
);
+-----+--------+
| tid | tname  |
+-----+--------+
|   3 | 王五   |
+-----+--------+


-- 20、查询有课程成绩小于60分的同学的学号、姓名；
select
    sid,
    sname
from
    student
where
    sid in (
        select
            distinct student_id
        from
            score
        where
            score.score < 60
    );
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 乔丹   |
|   3 | 科比   |
|   4 | curry  |
|   5 | james  |
|   6 | 李瑞   |
|   7 | 白雪   |
|   8 | 无敌   |
|   9 | 天剑   |
|  10 | egon   |
+-----+--------+

-- 21、查询没有学全所有课的同学的学号、姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        student_id
    from
        score
    group by student_id
    having count(course_id) < (
        select
            count(cid)
        from
            course
        )
    );
+-----+--------+
| sid | sname  |
+-----+--------+
|   4 | curry  |
|   5 | james  |
|   6 | 李瑞   |
|   7 | 白雪   |
|   8 | 无敌   |
|   9 | 天剑   |
|  10 | egon   |
|  11 | alex   |
+-----+--------+

-- 22、查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        distinct student_id
    from
        score
    where course_id in (
        select
            course_id   # 找出学号1锁学得所有课程
        from
            score
        where
            student_id=1
        ) and student_id!=1   # 排除掉学号为1的学生
    );
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾弗森    |
|   3 | 科比      |
|   4 | curry     |
|   5 | james     |
|   6 | 李瑞      |
|   7 | 白雪      |
|   8 | 无敌      |
|   9 | 天剑      |
|  10 | egon      |
|  11 | alex      |
+-----+-----------+

-- 23、查询至少学过学号为“1”同学所选课程中任意一门课的其他同学学号和姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        distinct student_id
    from
        score
    where course_id in (
        select
            course_id   # 找出学号1锁学得所有课程
        from
            score
        where
            student_id=1
        ) and student_id!=1   # 排除掉学号为1的学生
    );
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾弗森    |
|   3 | 科比      |
|   4 | curry     |
|   5 | james     |
|   6 | 李瑞      |
|   7 | 白雪      |
|   8 | 无敌      |
|   9 | 天剑      |
|  10 | egon      |
|  11 | alex      |
+-----+-----------+

-- 24、查询和“2”号同学学习的课程完全相同的其他同学的学号和姓名；
select
    sid,
    sname
from
    student
where
    sid in (
        select
            score.student_id
        from
            score
        inner join
            (select
                course_id  # 课程id
            from
                score
            where
                student_id = 2) as t1
        where
            score.course_id = t1.course_id
        and
            score.student_id != 2
        group by
            score.student_id
        having
            count(score.course_id) = (
                select    # 学号2所学课程总数
                    count(course_id)
                from
                    score
                where
                    student_id =2
                )
            );
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 乔丹   |
|   3 | 科比   |
+-----+--------+

-- 25、删除学习“张三”老师课的score表记录；
select
    course.cid
from
    course
left join
    teacher
on course.teacher_id=teacher.tid
where
    teacher.tname='张三';
+-----+
| cid |
+-----+
|   1 |
|   2 |
+-----+
# 删除course_id为1，2的记录
delete from
    score
where
    course_id in (
        select
            course.cid
        from
            course
        left join
            teacher
        on course.teacher_id=teacher.tid
        where
            teacher.tname='张三'
        );
+-----+------------+-----------+-------+
| sid | student_id | course_id | score |
+-----+------------+-----------+-------+
|   3 |          1 |         3 |    58 |
|   4 |          1 |         4 |    71 |
|   5 |          1 |         5 |    68 |
|   6 |          1 |         6 |   100 |
|   9 |          2 |         3 |    71 |
|  10 |          2 |         4 |    68 |
|  11 |          2 |         5 |    92 |
|  12 |          2 |         6 |    88 |
|  15 |          3 |         3 |    72 |
|  16 |          3 |         4 |    88 |
|  17 |          3 |         5 |    92 |
|  18 |          3 |         6 |    12 |
|  20 |          4 |         4 |    78 |
|  21 |          4 |         5 |    34 |
|  23 |          5 |         4 |    38 |
|  24 |          5 |         5 |    44 |
|  26 |          6 |         4 |    32 |
|  27 |          6 |         5 |     0 |
|  29 |          7 |         3 |    60 |
|  30 |          7 |         6 |    45 |
|  32 |          8 |         3 |    65 |
|  33 |          8 |         6 |    99 |
|  35 |          9 |         3 |    69 |
|  36 |          9 |         5 |    78 |
|  38 |         10 |         3 |    69 |
|  39 |         10 |         5 |    90 |
|  41 |         11 |         3 |    89 |
|  42 |         11 |         5 |   100 |
+-----+------------+-----------+-------+

-- 26、向score表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“2”课程的同学学号；②插入“2”号课程的平均成绩；
select
    sid
from
    student
where
    sid not in (
        select
            student_id
        from
            score
        where
            course_id =2
        );
+-----+
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
+-----+
select
    avg(score) as avg_score
from
    score
where
    course_id = 2;
+-----------+
| avg_score |
+-----------+
|      NULL |
+-----------+

insert into score(student_id, course_id, score)
select
    t1.sid,
    2,
    t2.avg_score
from
    (select
        sid
    from
        student
    where
        sid not in (
            select
                student_id
            from
                score
            where
                course_id =2
            )
    ) as t1,
    (select
        avg(score) as avg_score
    from
        score
    where
        course_id = 2
    ) as t2;
# 增加以下记录
+-----+------------+-----------+-------+
| sid | student_id | course_id | score |
+-----+------------+-----------+-------+
|   3 |          1 |         3 |    58 |
.......
|
|  42 |         11 |         5 |   100 |
|  43 |          1 |         2 |  NULL |
|  44 |          2 |         2 |  NULL |
|  45 |          3 |         2 |  NULL |
|  46 |          4 |         2 |  NULL |
|  47 |          5 |         2 |  NULL |
|  48 |          6 |         2 |  NULL |
|  49 |          7 |         2 |  NULL |
|  50 |          8 |         2 |  NULL |
|  51 |          9 |         2 |  NULL |
|  52 |         10 |         2 |  NULL |
|  53 |         11 |         2 |  NULL |
+-----+------------+-----------+-------+
# 将这些空值都修改为73

-- 27、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
# 这个题难度很大
select
    main_score.student_id,
    (select
        score.score
    from
        score
    left join
        course
    on score.course_id=course.cid
    where
        course.cname='语文'
    and score.student_id=main_score.student_id) as chinese,
    (select
        score.score
    from
        score
    left join
        course
    on score.course_id=course.cid
    where
        course.cname='数学'
    and score.student_id=main_score.student_id) as math,
    (select
        score.score
    from
        score
    left join
        course
    on score.course_id=course.cid
    where
        course.cname='英语'
    and score.student_id=main_score.student_id) as english,
    count(main_score.course_id),
    avg(main_score.score)
from
    score as main_score
group by
    main_score.student_id
order by        # 注意order的拼写
    avg(main_score.score) ASC;
+------------+---------+------+---------+-----------------------------+-----------------------+
| student_id | chinese | math | english | count(main_score.course_id) | avg(main_score.score) |
+------------+---------+------+---------+-----------------------------+-----------------------+
|          6 |      32 |    0 |    NULL |                           3 |               35.0000 |
|          5 |      38 |   44 |    NULL |                           3 |               51.6667 |
|          7 |    NULL | NULL |    NULL |                           3 |               59.3333 |
|          4 |      78 |   34 |    NULL |                           3 |               61.6667 |
|          3 |      88 |   92 |    NULL |                           5 |               67.4000 |
|          9 |    NULL |   78 |    NULL |                           3 |               73.3333 |
|          1 |      71 |   68 |    NULL |                           5 |               74.0000 |
|         10 |    NULL |   90 |    NULL |                           3 |               77.3333 |
|          2 |      68 |   92 |    NULL |                           5 |               78.4000 |
|          8 |    NULL | NULL |    NULL |                           3 |               79.0000 |
|         11 |    NULL |  100 |    NULL |                           3 |               87.3333 |
+------------+---------+------+---------+-----------------------------+-----------------------+


-- 28、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select
    course_id,
    max(score.score) as max_score,
    min(score.score) as min_score
from
    course
left join
    score
on course.cid=score.course_id
group by
    score.course_id;
+-----------+-----------+-----------+
| course_id | max_score | min_score |
+-----------+-----------+-----------+
|      NULL |      NULL |      NULL |
|         2 |        73 |        73 |
|         3 |        89 |        58 |
|         4 |        88 |        32 |
|         5 |       100 |         0 |
|         6 |       100 |        12 |
+-----------+-----------+-----------+

-- 29、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
select
    course_id,
    avg(score) as avg_score
from
    score
group by
    course_id
order by
    avg(score) desc;
+-----------+-----------+
| course_id | avg_score |
+-----------+-----------+
|         2 |   73.0000 |
|         3 |   69.1250 |
|         6 |   68.8000 |
|         5 |   66.4444 |
|         4 |   62.5000 |
+-----------+-----------+

-- 30、课程平均分从高到低显示（显示任课老师);
select
    t2.cid,
    t2.cname,
    t2.avg_score,
    teacher.tname
from
    teacher
right join (
    select
        course.cid,
        course.cname,
        t1.avg_score,
        course.teacher_id
    from
        course
    inner join (
        select
            course_id,
            avg(score) avg_score
        from
            score
        group by
            course_id
        ) as t1
    on course.cid=t1.course_id
) as t2
on teacher.tid=t2.teacher_id
order by
    t2.avg_score desc;
+-----+--------+-----------+--------+
| cid | cname  | avg_score | tname  |
+-----+--------+-----------+--------+
|   2 | 体育   |   73.0000 | 张三   |
|   3 | 物理   |   69.1250 | 李四   |
|   6 | 外语   |   68.8000 | 马七   |
|   5 | 数学   |   66.4444 | 赵六   |
|   4 | 语文   |   62.5000 | 王五   |
+-----+--------+-----------+--------+

-- 31、查询各科成绩前三名的记录(不考虑成绩并列情况)
select
    score.sid,score.course_id,score.score,T.first_num,T.second_num
from
    score
left join (
    select
        sid,
        (select
            score
        from
            score as s2
        where s2.course_id = s1.course_id
        order by score desc
        limit 0,1) as first_num,
        (select
            score
        from
            score as s2
        where s2.course_id = s1.course_id
        order by score desc
        limit 3,1) as second_num
    from
        score as s1
    ) as T
on score.sid =T.sid
where score.score <= T.first_num and score.score >= T.second_num;
+-----+-----------+-------+-----------+------------+
| sid | course_id | score | first_num | second_num |
+-----+-----------+-------+-----------+------------+
|  43 |         2 |    73 |        73 |         73 |
|  44 |         2 |    73 |        73 |         73 |
|  45 |         2 |    73 |        73 |         73 |
|  46 |         2 |    73 |        73 |         73 |
|  47 |         2 |    73 |        73 |         73 |
|  48 |         2 |    73 |        73 |         73 |
|  49 |         2 |    73 |        73 |         73 |
|  50 |         2 |    73 |        73 |         73 |
|  51 |         2 |    73 |        73 |         73 |
|  52 |         2 |    73 |        73 |         73 |
|  53 |         2 |    73 |        73 |         73 |
|   9 |         3 |    71 |        89 |         69 |
|  15 |         3 |    72 |        89 |         69 |
|  35 |         3 |    69 |        89 |         69 |
|  38 |         3 |    69 |        89 |         69 |
|  41 |         3 |    89 |        89 |         69 |
|   4 |         4 |    71 |        88 |         68 |
|  10 |         4 |    68 |        88 |         68 |
|  16 |         4 |    88 |        88 |         68 |
|  20 |         4 |    78 |        88 |         68 |
|  11 |         5 |    92 |       100 |         90 |
|  17 |         5 |    92 |       100 |         90 |
|  39 |         5 |    90 |       100 |         90 |
|  42 |         5 |   100 |       100 |         90 |
|   6 |         6 |   100 |       100 |         45 |
|  12 |         6 |    88 |       100 |         45 |
|  30 |         6 |    45 |       100 |         45 |
|  33 |         6 |    99 |       100 |         45 |
+-----+-----------+-------+-----------+------------+
# 需要进一步改进
select
    course_id,
    (select
        score
    from
        score as s2
    where s2.course_id = s1.course_id
    order by score desc
    limit 1) as first_num,
    (select
        score
    from
        score as s2
    where s2.course_id = s1.course_id
    order by score desc
    limit 1,1) as secend_num,
    (select
        score
    from
        score as s2
    where s2.course_id = s1.course_id
    order by score desc
    limit 2,1) as third_num
from
    score as s1;
+-----------+-----------+------------+-----------+
| course_id | first_num | secend_num | third_num |
+-----------+-----------+------------+-----------+
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         2 |        73 |         73 |        73 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         3 |        89 |         72 |        71 |
|         4 |        88 |         78 |        71 |
|         4 |        88 |         78 |        71 |
|         4 |        88 |         78 |        71 |
|         4 |        88 |         78 |        71 |
|         4 |        88 |         78 |        71 |
|         4 |        88 |         78 |        71 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         5 |       100 |         92 |        92 |
|         6 |       100 |         99 |        88 |
|         6 |       100 |         99 |        88 |
|         6 |       100 |         99 |        88 |
|         6 |       100 |         99 |        88 |
|         6 |       100 |         99 |        88 |
+-----------+-----------+------------+-----------+

select
    course_id

from
    (select
        course_id,
        (select
            score
        from
            score as s2
        where s2.course_id = s1.course_id
        order by score desc
        limit 1) as first_num,
        (select
            score
        from
            score as s2
        where s2.course_id = s1.course_id
        order by score desc
        limit 1,1) as secend_num,
        (select
            score
        from
            score as s2
        where s2.course_id = s1.course_id
        order by score desc
        limit 2,1) as third_num
    from
        score as s1
    ) as T
group by course_id;




-- 32、查询每门课程被选修的学生数；
select
    course_id,
    count(student_id)
from
    score
group by
    course_id;
+-----------+-------------------+
| course_id | count(student_id) |
+-----------+-------------------+
|         2 |                11 |
|         3 |                 8 |
|         4 |                 6 |
|         5 |                 9 |
|         6 |                 5 |
+-----------+-------------------+

-- 33、查询选修了2门以上课程的全部学生的学号和姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        student_id
    from
        score
    group by
        student_id
    having count(course_id) > 2
    );
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾弗森    |
|   3 | 科比      |
|   4 | curry     |
|   5 | james     |
|   6 | 李瑞      |
|   7 | 白雪      |
|   8 | 无敌      |
|   9 | 天剑      |
|  10 | egon      |
|  11 | alex      |
+-----+-----------+

-- 34、查询男生、女生的人数，按倒序排列；
select
    gender,
    count(sid)
from
    student
group by gender
order by count(sid) desc;
+--------+------------+
| gender | count(sid) |
+--------+------------+
| 男     |          6 |
| 女     |          5 |
+--------+------------+

-- 35、查询姓“张”的学生名单；
select
    *
from
    student
where
    sname='张%';
Empty set (0.00 sec)

-- 36、查询同名同姓学生名单，并统计同名人数；
select
    sname,
    count(sid)
from
    student
group by
    sname
having
    count(sid) > 1;
Empty set (0.00 sec)

-- 37、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
select
    course_id,
    avg(score)
from
    score
group by
    course_id
order by
    avg(score),     # 两种排序规则需要用逗号分隔
    course_id DESC;
+-----------+------------+
| course_id | avg(score) |
+-----------+------------+
|         4 |    62.5000 |
|         5 |    66.4444 |
|         6 |    68.8000 |
|         3 |    69.1250 |
|         2 |    73.0000 |
+-----------+------------+

-- 38、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
select
    student.sname,
    score.score
from
    score
inner join
    student
on score.student_id=student.sid
where score.course_id in (
    select
        cid
    from
        course
    where
        cname='数学'
    );
+-----------+-------+
| sname     | score |
+-----------+-------+
| 乔丹      |    68 |
| 艾弗森    |    92 |
| 科比      |    92 |
| curry     |    34 |
| james     |    44 |
| 李瑞      |     0 |
| 天剑      |    78 |
| egon      |    90 |
| alex      |   100 |
+-----------+-------+

-- 39、查询课程编号为“3”且课程成绩在80分以上的学生的学号和姓名；
select
    sid,
    sname
from
    student
where sid in (
    select
        student_id
    from
        score
    where
        course_id=3
    and score>=80
    );
+-----+-------+
| sid | sname |
+-----+-------+
|  11 | alex  |
+-----+-------+

-- 40、求选修了课程的学生人数
select
    course_id,
    count(student_id)
from
    score
group by
    course_id;
+-----------+-------------------+
| course_id | count(student_id) |
+-----------+-------------------+
|         2 |                11 |
|         3 |                 8 |
|         4 |                 6 |
|         5 |                 9 |
|         6 |                 5 |
+-----------+-------------------+

-- 41、查询选修“王五”老师所授课程的学生中，成绩最高和最低的学生姓名及其成绩；
select
    *
from
    (select
        *
    from
        student
    inner join
        (select
            student_id,
            score
        from
            score
        where
            course_id in (
                select
                    cid
                from
                    teacher
                inner join
                    course
                on teacher.tid=course.teacher_id
                where
                    tname='王五'
                )
        ) as t1
    on student.sid=t1.student_id
    order by
        score
    limit 1
    ) as t2
union
select
    *
from
    (select
        *
    from
        student
    inner join
        (select
            student_id,
            score
        from
            score
        where
            course_id in (
                select
                    cid
                from
                    teacher
                inner join
                    course
                on teacher.tid=course.teacher_id
                where
                    tname='王五'
                )
        ) as t1
    on student.sid=t1.student_id
    order by
        score DESC
    limit 1
    ) as t3;
+-----+--------+--------+----------+------------+-------+
| sid | sname  | gender | class_id | student_id | score |
+-----+--------+--------+----------+------------+-------+
|   6 | 李瑞   | 女     |        4 |          6 |    32 |
|   3 | 科比   | 男     |        2 |          3 |    88 |
+-----+--------+--------+----------+------------+-------+

-- 42、查询各个课程及相应的选修人数；
select
    cid,
    cname,
    t1.stu_num
from
    course
right join
    (select
        course_id,
        count(student_id) as stu_num
    from
        score
    group by
        course_id) as t1
on course.cid=t1.course_id;
+------+--------+---------+
| cid  | cname  | stu_num |
+------+--------+---------+
|    2 | 体育   |      11 |
|    3 | 物理   |       8 |
|    4 | 语文   |       6 |
|    5 | 数学   |       9 |
|    6 | 外语   |       5 |
+------+--------+---------+

-- 43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
select
    *
from
    score
where
    score in (
        select
            score   # 找到不同课程但是有相同分数的成绩数值
        from
            score
        group by
            score
        having
            count(course_id)>1
        )
order by score;
+-----+------------+-----------+-------+
| sid | student_id | course_id | score |
+-----+------------+-----------+-------+
|   5 |          1 |         5 |    68 |
|  10 |          2 |         4 |    68 |
|  35 |          9 |         3 |    69 |
|  38 |         10 |         3 |    69 |
|   4 |          1 |         4 |    71 |
|   9 |          2 |         3 |    71 |
|  43 |          1 |         2 |    73 |
|  44 |          2 |         2 |    73 |
|  45 |          3 |         2 |    73 |
|  46 |          4 |         2 |    73 |
|  47 |          5 |         2 |    73 |
|  48 |          6 |         2 |    73 |
|  49 |          7 |         2 |    73 |
|  50 |          8 |         2 |    73 |
|  51 |          9 |         2 |    73 |
|  52 |         10 |         2 |    73 |
|  53 |         11 |         2 |    73 |
|  20 |          4 |         4 |    78 |
|  36 |          9 |         5 |    78 |
|  12 |          2 |         6 |    88 |
|  16 |          3 |         4 |    88 |
|  11 |          2 |         5 |    92 |
|  17 |          3 |         5 |    92 |
|   6 |          1 |         6 |   100 |
|  42 |         11 |         5 |   100 |
+-----+------------+-----------+-------+

-- 44、查询每门课程成绩最好的前两名学生id和姓名；
select
    student.sid,
    student.sname,
    t2.course_id,
    t2.score,
    t2.first_score,
    t2.second_score
from
    student
inner join (                    # 这里会出现成绩相同的情况，录入了超过了两名的学生！！
    select
        score.student_id,
        score.course_id,
        score.score,
        t1.first_score,
        t1.second_score
    from
        score
    inner join (
        select
            s1.sid,
            (select s2.score from score as s2 where s1.course_id = s2.course_id order by s2.score desc limit 0,1) as first_score,
            (select s3.score from score as s3 where s1.course_id = s3.course_id order by s3.score desc limit 1,1) as second_score
        from
            score as s1
    ) as t1 on score.sid = t1.sid
    where
        score.score in (           # ？？在这，会超过两个！！
            t1.first_score,
            t1.second_score
        )
) as t2 on student.sid = t2.student_id;
+-----+-----------+-----------+-------+-------------+--------------+
| sid | sname     | course_id | score | first_score | second_score |
+-----+-----------+-----------+-------+-------------+--------------+
|   1 | 乔丹      |         2 |    73 |          73 |           73 |
|   2 | 艾弗森    |         2 |    73 |          73 |           73 |
|   3 | 科比      |         2 |    73 |          73 |           73 |
|   4 | curry     |         2 |    73 |          73 |           73 |
|   5 | james     |         2 |    73 |          73 |           73 |
|   6 | 李瑞      |         2 |    73 |          73 |           73 |
|   7 | 白雪      |         2 |    73 |          73 |           73 |
|   8 | 无敌      |         2 |    73 |          73 |           73 |
|   9 | 天剑      |         2 |    73 |          73 |           73 |
|  10 | egon      |         2 |    73 |          73 |           73 |
|  11 | alex      |         2 |    73 |          73 |           73 |
|   3 | 科比      |         3 |    72 |          89 |           72 |
|  11 | alex      |         3 |    89 |          89 |           72 |
|   3 | 科比      |         4 |    88 |          88 |           78 |
|   4 | curry     |         4 |    78 |          88 |           78 |
|   2 | 艾弗森    |         5 |    92 |         100 |           92 |
|   3 | 科比      |         5 |    92 |         100 |           92 |
|  11 | alex      |         5 |   100 |         100 |           92 |
|   1 | 乔丹      |         6 |   100 |         100 |           99 |
|   8 | 无敌      |         6 |    99 |         100 |           99 |
+-----+-----------+-----------+-------+-------------+--------------+

-- 45、检索至少选修两门课程的学生学号；
select
    student_id
from
    score
group by
    student_id
having
    count(course_id)>=2;
+------------+
| student_id |
+------------+
|          1 |
|          2 |
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
+------------+


-- 46、查询没有学生选修的课程的课程号和课程名；
select
    cid,
    cname
from
    course
where
    cid not in (
        select
            course_id
        from
            score
        group by
            course_id
        );
+-----+--------+
| cid | cname  |
+-----+--------+
|   1 | 生物   |
+-----+--------+

-- 47、查询没带过任何班级的老师id和姓名；
select
    tid,
    tname
from
    teacher
where
    tid not in(
        select
            tid
        from
            teach2cls
        group by
            tid
        );
Empty set (0.00 sec)

-- 48、查询有两门以上课程超过80分的学生id及其平均成绩；
select
    student_id,
    avg(score) as avg_score
from
    score
where  score.student_id in
    (select
        student_id    # 找到有两门课大于80的学号
    from
        (select
            *
        from
            score
        where
            score>80) as t1
    group by
        student_id
    having
        count(course_id) >= 2
    )
group by student_id;
+------------+-----------+
| student_id | avg_score |
+------------+-----------+
|          2 |   78.4000 |
|          3 |   67.4000 |
|         11 |   87.3333 |
+------------+-----------+

-- 49、检索“3”课程分数小于60，按分数降序排列的同学学号；
select
    student_id
from
    score
where
    course_id=3
and score<60
order by score DESC;
+------------+
| student_id |
+------------+
|          1 |
+------------+

-- 50、删除编号为“2”的同学的“1”课程的成绩；
select
    sid
from
    score
where
    student_id=2
    and course_id=1;

delete from
    score
where
    sid in (
        select
            sid
        from
            score
        where
            student_id=2
            and course_id=1
        );
ERROR 1093 (HY000): You can't specify target table 'score' for update in FROM clause'
delete from
    score
where
    sid in (
        select
            t1.sid
        from (
            select
                sid
            from
                score
            where
                student_id=2
                and course_id=1
            ) as t1
        );
Query OK, 0 rows affected (0.00 sec)

-- 51、查询同时选修了物理课和生物课的学生id和姓名；
select
    cid
from
    course
where
    cname='物理'
    or cname='生物';
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   3 | 物理   |          2 |
+-----+--------+------------+

select
    sid,
    sname
from
    student
where
    sid in (
        select
            student_id
        FROM
            score
        where
            course_id in (
                select
                    cid
                from
                    course
                where
                    cname='物理'
                    or cname='生物'
                )
        group by
            student_id
        having
            count(course_id)=2
        );
Empty set (0.00 sec)





