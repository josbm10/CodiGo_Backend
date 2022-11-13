const {Router} = require('express');
const router = Router();

const { getAll, create, update ,deletePry} = require('../controllers/project.controller');



router.get('/',getAll);
router.post('/',create);
router.put('/:id',update);
router.delete('/:id',deletePry);

module.exports = router;

