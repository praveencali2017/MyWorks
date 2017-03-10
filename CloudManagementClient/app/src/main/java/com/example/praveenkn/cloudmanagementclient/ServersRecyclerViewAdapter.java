package com.example.praveenkn.cloudmanagementclient;

import android.app.Activity;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Handler;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.TextView;

import com.example.praveenkn.cloudmanagementclient.Models.Server;

import com.example.praveenkn.cloudmanagementclient.ItemFragment_Servers.OnListFragmentServersInteractionListener;

import org.json.JSONException;

import java.util.List;


public class ServersRecyclerViewAdapter extends RecyclerView.Adapter<ServersRecyclerViewAdapter.ViewHolder> {

    private final List<Server> mValues;
    private final OnListFragmentServersInteractionListener mListener;
    private final Handler mListenerForBtn;
    private final Handler mListenerForEdit;
    private Context context;
    public ServersRecyclerViewAdapter(List<Server> items, OnListFragmentServersInteractionListener listener,Handler listenerForBtn,Handler listenerForEdit, Context context) {
        mValues = items;
        mListener = listener;
        mListenerForEdit=listenerForEdit;
        this.mListenerForBtn=listenerForBtn;
        this.context=context;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.fragment_listitems_servers, parent, false);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(final ViewHolder holder, int position) {
        holder.mItem = mValues.get(position);
        holder.mBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ServiceComponent serviceComponent=new ServiceComponent();
                serviceComponent.setHandler(mListenerForBtn);
                serviceComponent.execute(UtilityCloud.serversRequestUrl+"/"+holder.mItem.serverUUID,"DELETE");
            }
        });
        holder.mEditBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               setDialogBuilder(holder.mItem.serverUUID);
            }
        });
        holder.mContentView.setText(mValues.get(position).serverName);

        holder.mView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (null != mListener) {
                    // Notify the active callbacks interface (the activity, if the
                    // fragment is attached to one) that an item has been selected.
                    mListener.onListFragmentInteraction(holder.mItem);
                }
            }
        });

    }
    private void setDialogBuilder(final String serverUUID){
        AlertDialog.Builder builder= new AlertDialog.Builder(context);
        builder.setTitle("Edit Server");
        View inflatedView=LayoutInflater.from(context).inflate(R.layout.dialog_view,null, false);
        final AutoCompleteTextView input = (AutoCompleteTextView) inflatedView.findViewById(R.id.serverNameDialog);
        // Specify the type of input expected; this, for example, sets the input as a password, and will mask the text
        builder.setView(inflatedView);

        // Set up the buttons
        builder.setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
                ServiceComponent serviceComponent=null;
                try {
                    String m_Text = input.getText().toString();
                    serviceComponent=new ServiceComponent();
                    serviceComponent.createServerEdit(m_Text);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                serviceComponent.setHandler(mListenerForEdit);
                serviceComponent.execute(UtilityCloud.serversRequestUrl+"/"+serverUUID,"PUT");
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
    public int getItemCount() {
        return mValues.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        public final View mView;
        public final Button mBtn;
        public final Button mEditBtn;
        public final TextView mContentView;
        public Server mItem;

        public ViewHolder(View view) {
            super(view);
            mView = view;
            mBtn = (Button) view.findViewById(R.id.serverAddBtn);
            mEditBtn=(Button) view.findViewById(R.id.serverEditBtn);
            mContentView = (TextView) view.findViewById(R.id.serverNameTextView);
        }

        @Override
        public String toString() {
            return super.toString() + " '" + mContentView.getText() + "'";
        }
    }
}
