const mongoose = require("mongoose");

const diagnosticReportSchema = new mongoose.Schema({
  issueTitle: String,
  errorCode: String,
  symptoms: String,
  probableCause: String,
  severity: { type: String, enum: ["Low", "Medium", "High", "Critical"] },
});

const inspectionItemSchema = new mongoose.Schema({
  status: { type: String, enum: ["Good", "Issue", "Critical"] },
  notes: String,
});

const maintenanceFormSchema = new mongoose.Schema({
  garage: { type: mongoose.Schema.Types.ObjectId, ref: "Organization", required: true },
  officer: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },

  // Intake
  plateNumber: String,
  chassisNumber: { type: String, required: true },
  engineNumber: String,
  vehicleMake: String,
  vehicleModel: String,
  year: Number,
  fuelType: String,
  currentOdometer: Number,
  color: String,

  // Inspection
  inspection: {
    type: Map,
    of: inspectionItemSchema,
  },

  // Diagnostics
  diagnosticReports: [diagnosticReportSchema],

  // Engine Diagnostics
  checkEngineLight: Boolean,
  detectedErrorCodes: String,
  engineCondition: String,
  engineNoise: String,
  oilLeak: String,
  smokeColor: String,
  overheating: Boolean,
  sensorIssues: String,

  // Summary
  overallCondition: String,
  mainProblems: String,
  recommendedFixes: String,
  mechanicNotes: String,

  createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model("MaintenanceForm", maintenanceFormSchema);
