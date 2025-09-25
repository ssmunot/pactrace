import streamlit as st
from packet_trace import PacketTraceJob

st.set_page_config(page_title="Packet Trace Collector", page_icon=":satellite:", layout="centered")

# Session state for storing trace job info
if "trace_job" not in st.session_state:
    st.session_state.trace_job = None
if "trace_started" not in st.session_state:
    st.session_state.trace_started = False

def main():
    st.title("📡 Packet Trace Collector")

    if not st.session_state.trace_started:
        with st.form(key="trace_form"):
            st.subheader("Trace Input Parameters")
            node_name = st.text_input("Node Name", max_chars=30)
            port = st.number_input("Port", min_value=1, max_value=65535, value=1234)
            file_size = st.number_input("File Size (MB)", min_value=1, max_value=10000, value=100)
            buffer_size = st.number_input("Buffer Size (KB)", min_value=1, max_value=1048576, value=1024)
            host_address = st.text_input("Host Address (e.g., 192.168.1.10)")
            
            rolling = st.checkbox("Collect Rolling Packet Traces?")
            num_traces = None
            if rolling:
                num_traces = st.number_input("Number of Traces in Rolling", min_value=1, max_value=100, value=5)

            start_btn = st.form_submit_button("🚀 Start Packet Trace")
            
            if start_btn:
                if not node_name or not host_address:
                    st.warning("Please provide all required fields.")
                else:
                    st.session_state.trace_job = PacketTraceJob(
                        node_name=node_name,
                        port=port,
                        file_size=file_size,
                        buffer_size=buffer_size,
                        host_address=host_address,
                        rolling=rolling,
                        num_traces=num_traces if rolling else None
                    )
                    st.session_state.trace_job.start()
                    st.session_state.trace_started = True
                    st.success("Packet trace started!")

    else:
        job = st.session_state.trace_job
        st.subheader("🟢 Packet Trace Collection Running")
        info = {
            "Node Name": job.node_name,
            "Port": job.port,
            "File Size (MB)": job.file_size,
            "Buffer Size (KB)": job.buffer_size,
            "Host Address": job.host_address,
            "Rolling": "Yes" if job.rolling else "No",
            "Number of Rolling Traces": job.num_traces if job.rolling else "-"
        }
        st.table(list(info.items()))

        st.info("Tracing is running in the background. You can stop it at any time.")
        if st.button("🛑 Stop Packet Trace"):
            job.stop()
            st.session_state.trace_started = False
            st.success("Packet trace stopped.")

if __name__ == "__main__":
    main()
