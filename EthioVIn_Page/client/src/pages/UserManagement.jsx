import { useState, useEffect } from "react";
import api from "../api/axiosInstance";

export default function UserManagement() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "EventManager",
    assignedEventId: "",
  });

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const { data } = await api.get("/admin/events");
        setEvents(data);
        if (data.length > 0) setForm((prev) => ({ ...prev, assignedEventId: data[0]._id }));
      } catch (err) {
        console.error("Failed to load events", err);
      }
    };
    fetchEvents();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await api.post("/admin/users", form);
      alert("User created successfully");
      setForm({ ...form, name: "", email: "", password: "" }); // Reset fields
    } catch (err) {
      alert(err.response?.data?.message || "Failed to create user");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <div className="card bg-base-100 border-4 border-base-content shadow-neo dark:shadow-neo-dark rounded-none">
        <div className="card-body">
          <h2 className="card-title text-3xl font-black uppercase italic tracking-tighter mb-4">
            Staff <span className="text-primary">Provisioning</span>
          </h2>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="form-control">
              <label className="label">
                <span className="label-text font-bold uppercase">Name</span>
              </label>
              <input type="text" required className="input input-bordered border-2 border-base-content rounded-none" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} />
            </div>

            <div className="form-control">
              <label className="label">
                <span className="label-text font-bold uppercase">Email</span>
              </label>
              <input
                type="email"
                required
                className="input input-bordered border-2 border-base-content rounded-none"
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
              />
            </div>

            <div className="form-control">
              <label className="label">
                <span className="label-text font-bold uppercase">Temporary Password</span>
              </label>
              <input
                type="password"
                required
                className="input input-bordered border-2 border-base-content rounded-none"
                value={form.password}
                onChange={(e) => setForm({ ...form, password: e.target.value })}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="form-control">
                <label className="label">
                  <span className="label-text font-bold uppercase">Role</span>
                </label>
                <select className="select select-bordered border-2 border-base-content rounded-none font-bold" value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })}>
                  <option value="EventManager">Event Manager</option>
                  <option value="Scanner">Scanner (Door Staff)</option>
                </select>
              </div>

              <div className="form-control">
                <label className="label">
                  <span className="label-text font-bold uppercase">Assign To Event</span>
                </label>
                <select
                  className="select select-bordered border-2 border-base-content rounded-none font-bold"
                  required
                  value={form.assignedEventId}
                  onChange={(e) => setForm({ ...form, assignedEventId: e.target.value })}
                >
                  {events.map((ev) => (
                    <option key={ev._id} value={ev._id}>
                      {ev.title}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <button
              disabled={loading}
              className={`btn btn-primary w-full mt-4 rounded-none border-2 border-base-content font-black text-lg shadow-neo dark:shadow-neo-dark ${loading ? "loading" : ""}`}
            >
              CREATE ACCOUNT
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
