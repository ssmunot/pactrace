import streamlit as st
from ontap_trace import start_packet_trace, stop_packet_trace

st.set_page_config(page_title="ONTAP Packet Trace", layout="centered")

def main():
    st.title("🖧 ONTAP Packet Trace Collector")

    st.markdown("Enter the details below to collect a packet trace from your ONTAP System Manager.")

    with st.form("packet_trace_form"):
        node_name = st.text_input("Node Name")
        port = st.text_input("Port")
        address = st.text_input("Address")
        file_size = st.number_input("File Size (MB)", min_value=1)
        buffer_size = st.number_input("Buffer Size (KB)", min_value=1)
        host_address = st.text_input("Host Address")

        rolling_enabled = st.checkbox("Collect Rolling Packet Traces?")
        rolling_traces = None
        if rolling_enabled:
            rolling_traces = st.number_input("Number of Rolling Packet Traces", min_value=1)

        submitted = st.form_submit_button("Start Packet Trace")
        
    if submitted:
        # Call your function to start packet trace
        task_id = start_packet_trace(
            node_name, port, address, file_size, buffer_size, host_address, 
            rolling_enabled, rolling_traces
        )
        st.session_state['task_id'] = task_id
        st.success("Packet trace has started! ✨")
        st.switch_page("trace_status")  # This will redirect to another page

if __name__ == "__main__":
    main()
