const express = require("express");
const { protect, authorizeRoles } = require("../middleware/authMiddleware");
const { submitForm, getForms } = require("../controllers/maintainance.controller");

const router = express.Router();

router.post("/form", protect, authorizeRoles("garage_officer"), submitForm);
router.get("/forms", protect, authorizeRoles("garage_admin", "garage_officer", "super_admin"), getForms);

module.exports = router;
