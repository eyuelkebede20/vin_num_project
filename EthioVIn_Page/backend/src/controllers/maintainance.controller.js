const MaintenanceForm = require("../models/MaintenanceForm");
const User = require("../models/User");

const submitForm = async (req, res) => {
  try {
    const officer = await User.findById(req.user.id);
    if (!officer || !officer.organization) {
      return res.status(400).json({ error: "Officer organization not found." });
    }

    const newForm = await MaintenanceForm.create({
      ...req.body,
      garage: officer.organization,
      officer: officer._id,
    });

    res.status(201).json({ message: "Maintenance form submitted successfully.", formId: newForm._id });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Failed to submit maintenance form." });
  }
};

const getForms = async (req, res) => {
  try {
    const user = await User.findById(req.user.id);
    const forms = await MaintenanceForm.find({ garage: user.organization }).sort({ createdAt: -1 });
    res.json(forms);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch forms." });
  }
};

module.exports = { submitForm, getForms };
