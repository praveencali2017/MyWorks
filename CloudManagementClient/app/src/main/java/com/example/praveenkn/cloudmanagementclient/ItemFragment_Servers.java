package com.example.praveenkn.cloudmanagementclient;

import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v4.app.Fragment;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AutoCompleteTextView;
import android.widget.Button;

import com.example.praveenkn.cloudmanagementclient.Models.Server;


import org.json.JSONException;

import java.util.List;


public class ItemFragment_Servers extends Fragment {

    // TODO: Customize parameter argument names
    private static final String ARG_COLUMN_COUNT = "column-count";
    // TODO: Customize parameters
    private int mColumnCount = 1;
    private OnListFragmentServersInteractionListener mListener;
    public Handler delBtnHandler;
    private List<Server> servers;
    public Handler addBtnHandler;
    public Handler editBtnHandler;
    /**
     * Mandatory empty constructor for the fragment manager to instantiate the
     * fragment (e.g. upon screen orientation changes).
     */
    public ItemFragment_Servers() {
    }

    // TODO: Customize parameter initialization
    @SuppressWarnings("unused")
    public static ItemFragment_Servers newInstance(int columnCount) {
        ItemFragment_Servers fragment = new ItemFragment_Servers();
        Bundle args = new Bundle();
        args.putInt(ARG_COLUMN_COUNT, columnCount);
        fragment.setArguments(args);
        return fragment;
    }
    public  void setListItemsServers(List<Server> servers){
        this.servers=servers;
    }
    public  void setDeleteBtnHandler(Handler handler){
        this.delBtnHandler=handler;
    }
    public  void setAddBtnHandler(Handler handler){
        this.addBtnHandler=handler;
    }
    public void setEditBtnHandler(Handler handler){this.editBtnHandler=handler;}
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mColumnCount = getArguments().getInt(ARG_COLUMN_COUNT);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_item_list2, container, false);
       View view_sub=view.findViewById(R.id.serversListView);
        Button btn=(Button) view.findViewById(R.id.addServerBtn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setDialogBuilder();
            }
        });
        // Set the adapter
        if (view_sub instanceof RecyclerView) {
            Context context = view_sub.getContext();
            RecyclerView recyclerView = (RecyclerView) view_sub;
            if (mColumnCount <= 1) {
                recyclerView.setLayoutManager(new LinearLayoutManager(context));
            } else {
                recyclerView.setLayoutManager(new GridLayoutManager(context, mColumnCount));
            }
            recyclerView.setAdapter(new ServersRecyclerViewAdapter(servers, mListener,delBtnHandler,editBtnHandler,getContext()));
        }
        return view;
    }

private void setDialogBuilder(){
    AlertDialog.Builder builder= new AlertDialog.Builder(getContext());
    builder.setTitle("Create Server");
    View inflatedView=LayoutInflater.from(getContext()).inflate(R.layout.dialog_view, (ViewGroup) getView(), false);
    final AutoCompleteTextView input = (AutoCompleteTextView) inflatedView.findViewById(R.id.serverNameDialog);
    // Specify the type of input expected; this, for example, sets the input as a password, and will mask the text
    builder.setView(inflatedView);

    // Set up the buttons
    builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
        @Override
        public void onClick(DialogInterface dialog, int which) {
            dialog.dismiss();
           String m_Text = input.getText().toString();
            ServiceComponent serviceComponent=new ServiceComponent();
            serviceComponent.setHandler(addBtnHandler);
            try {
                serviceComponent.createServerObject(m_Text);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            serviceComponent.execute(UtilityCloud.serversRequestUrl,"POST");
        }
    });
    builder.setNegativeButton(android.R.string.cancel, new DialogInterface.OnClickListener() {
        @Override
        public void onClick(DialogInterface dialog, int which) {
            dialog.cancel();
        }
    });
    builder.show();
}
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnListFragmentServersInteractionListener) {
            mListener = (OnListFragmentServersInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnListFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p/>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnListFragmentServersInteractionListener {
        // TODO: Update argument type and name
        void onListFragmentInteraction(Server item);
    }
}