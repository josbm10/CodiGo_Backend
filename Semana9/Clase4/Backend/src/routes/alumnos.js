const  { Router } = require('express');
const router = Router();

const {getAll,create,getById} = require('../controllers/alumnos');
const validatorHandler = require('../middlewares/validator.handler');
const {createAlumnoSchema} = require('../schemas/alumnos');
const auth = require('../middlewares/auth');

router.route('/')
    .get(auth,getAll)
    .post(validatorHandler(createAlumnoSchema,'body'),create)

router.route('/:id')
    .get(getById)

module.exports = router;