--POBLADO DE DATOS
insert into tbl_bootcamp(bootcamp_nombre) values ('DESARROLLO WEB');
insert into tbl_alumno(alumno_id,alumno_nombre,alumno_email)
VALUES
(1,'DIEGO','diego@gmail.com'),
(2,'EDER','eder@gmail.com');

insert into tbl_matricula(matricula_id,bootcamp_id,matricula_grupo,matricula_fecregr,alumno_id)
VALUES
(1,1,'G11','2021-09-01',1),
(2,1,'G12',CURRENT_DATE(),2);

insert into tbl_curso(curso_nombre) VALUES
('HTML Y CSS'),
('JAVASCRIPT'),
('REACT.JS'),
('PYTHON'),
('NODE.JS');

insert into tbl_profesor(profesor_id,profesor_nombre) VALUES
(1,'SEBASTIAN YABIKU'),
(2,'CESAR MAYTA'),
(3,'DIEGO DE RIVERO');

insert into tbl_matricula_curso(matricula_curso_id,matricula_id,profesor_id,curso_id)
VALUES
(1,1,1,1),
(2,1,1,1),
(3,1,1,2),
(4,1,1,3),
(5,1,2,4),
(6,1,2,5),
(7,2,1,1),
(8,2,1,2),
(9,2,1,3),
(10,2,3,4),
(11,2,3,5)