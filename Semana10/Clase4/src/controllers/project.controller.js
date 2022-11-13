const projectController = {};
const Project = require("../models/Project");

projectController.getAll = async (req, res) => {
  try {
    const projects = await Project.findAll();
    res.json({
      status: true,
      content: projects,
    });
  } catch (error) {
    console.log(error);
    res.json({
      status: false,
      content: "ocurrio un problema",
    });
  }
};
projectController.create = async (req, res) => {
  const { name } = req.body;
  try {
    let newProject = await Project.create({ name });
    if (newProject) {
      return res.json({
        status: true,
        content: newProject,
      });
    }
  } catch (error) {
    console.log(error);
    res.status(500).json({
      status: false,
      content: "ocurrio un problema",
    });
  }
};
projectController.update = async (req, res) => {
  const { name } = req.body;
  const { id } = req.params;
  try {
    let updateProject = await Project.findByPk(id)

    if (updateProject) {
      updateProject.update({
        name
      });
      return res.json({
        status: true,
        content: updateProject,
      });
    }
  } catch (error) {
    console.log(error);
    res.status(500).json({
      status: false,
      content: "ocurrio un problema",
    });
  }
};
projectController.deletePry = async (req, res) => {
    const { id } = req.params;
    try {
      let deleteProject = await Project.findByPk(id)
  
      if (deleteProject) {
        deleteProject.destroy()
        return res.json({
          status: true,
          content: deleteProject,
        });
      }
    } catch (error) {
      console.log(error);
      res.status(500).json({
        status: false,
        content: "ocurrio un problema",
      });
    }
  };

module.exports = projectController;
