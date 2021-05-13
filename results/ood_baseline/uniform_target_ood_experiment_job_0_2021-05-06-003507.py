store = {}
store['timestamp']=1620257707
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=0']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=40
store['config']={'seed': 0, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4180450439453125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.85390043258667})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.207883358001709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.291226863861084})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6532, 'crossentropy': 2.2503056640625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 18105], ['id', 38686], ['id', 57768], ['id', 44589], ['id', 35063]], 'labels': [6, 0, 5, 0, 0], 'scores': [0.8763377666473389, 1.0522065162658691, 0.9763432145118713, 1.2519292831420898, 0.8152251839637756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.281111001968384})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.552518844604492})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.724557876586914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.9618725776672363})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6934, 'crossentropy': 2.090011328125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 4147], ['id', 11505], ['id', 25092], ['id', 49335], ['id', 30732]], 'labels': [8, 5, 0, 9, 8], 'scores': [0.7400401830673218, 0.7043412327766418, 0.8486685156822205, 0.8098176121711731, 0.828563928604126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.201460838317871})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.457420825958252})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.171370029449463})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5356976985931396})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6698, 'crossentropy': 1.9253955078125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1845], ['id', 39437], ['id', 48292], ['ood', 18628], ['id', 30344]], 'labels': [4, 1, 2, 6, 2], 'scores': [0.5815786719322205, 0.8796437382698059, 0.9472420811653137, 0.682518482208252, 0.8465670347213745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5649473667144775})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.7261961698532104})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.132530450820923})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.9381186962127686})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7322, 'crossentropy': 1.426321484375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 17621], ['id', 33333], ['id', 49055], ['id', 37109], ['id', 55438]], 'labels': [3, 2, 3, 8, 8], 'scores': [0.6112838387489319, 0.7678807377815247, 0.7331798672676086, 0.732020914554596, 0.6261024475097656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.3997067213058472})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.6040425300598145})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7160444259643555})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8589775562286377})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7715, 'crossentropy': 1.1812515625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 51650], ['id', 610], ['id', 2337], ['id', 375], ['id', 34035]], 'labels': [7, 5, 2, 2, 4], 'scores': [0.8576065301895142, 0.6396892070770264, 0.6878829598426819, 0.7087011933326721, 0.4641467332839966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2619314193725586})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.3118183612823486})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.4978916645050049})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2708327770233154})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 1.103773828125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34804], ['id', 8968], ['id', 8672], ['id', 18994], ['id', 8031]], 'labels': [8, 9, 3, 8, 8], 'scores': [0.7564430236816406, 0.7374588251113892, 0.6091117262840271, 0.5935332775115967, 0.7755162715911865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1742143630981445})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.188530683517456})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2576771974563599})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3829554319381714})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8327, 'crossentropy': 0.91617431640625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 24237], ['id', 30810], ['id', 26829], ['id', 42687], ['id', 48300]], 'labels': [6, 2, 7, 5, 3], 'scores': [0.6951833963394165, 0.6412862539291382, 0.610578179359436, 0.8449957370758057, 0.5730626583099365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9004554152488708})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0425735712051392})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.113802433013916})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1609188318252563})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8577, 'crossentropy': 0.8264435546875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 21952], ['id', 19298], ['id', 40766], ['id', 37293], ['id', 9948]], 'labels': [2, 6, 4, 3, 8], 'scores': [0.7920441627502441, 0.6876884698867798, 0.7758377194404602, 0.7513160109519958, 0.6328396797180176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8319792747497559})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9317871332168579})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9728264808654785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9634729623794556})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8629, 'crossentropy': 0.765058935546875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 14760], ['id', 49537], ['id', 33593], ['id', 15679], ['id', 23315]], 'labels': [2, 2, 2, 2, 0], 'scores': [0.6997772455215454, 0.8681017756462097, 0.6990157961845398, 0.8027454018592834, 0.8319536447525024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8761351108551025})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0192713737487793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9286615252494812})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.08443021774292})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8455, 'crossentropy': 0.84456279296875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 8353], ['id', 48548], ['id', 28368], ['id', 33694], ['id', 20470]], 'labels': [7, 9, 9, 3, 3], 'scores': [0.6495616436004639, 0.5859256982803345, 0.4730949401855469, 0.4838980436325073, 0.5494044423103333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9336980581283569})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9830470085144043})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.944737434387207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0922763347625732})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8484, 'crossentropy': 0.84616396484375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 28944], ['id', 40066], ['id', 23517], ['id', 52388], ['id', 26024]], 'labels': [2, 4, 3, 5, 5], 'scores': [0.5935300588607788, 0.47762662172317505, 0.4246689975261688, 0.6046513915061951, 0.5513129830360413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8673310279846191})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8385319709777832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8602018356323242})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.006394863128662})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9962043762207031})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8808, 'crossentropy': 0.745753662109375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 45056], ['id', 58318], ['id', 23490], ['ood', 55118], ['id', 38142]], 'labels': [8, 5, 3, 7, 8], 'scores': [0.6997876763343811, 0.7239611148834229, 0.656870424747467, 0.6398741006851196, 0.5102890729904175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.958941638469696})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9096724987030029})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9152647256851196})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0375475883483887})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9114305973052979})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8592, 'crossentropy': 0.813369580078125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22121], ['id', 42149], ['id', 7621], ['id', 51522], ['id', 12381]], 'labels': [6, 9, 7, 3, 5], 'scores': [0.7006229162216187, 0.5633648633956909, 0.661990225315094, 0.7952971458435059, 0.5823760628700256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8282410502433777})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7164378762245178})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.747138261795044})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7926928997039795})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8276551961898804})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8822, 'crossentropy': 0.706674853515625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 48306], ['ood', 8352], ['id', 45250], ['id', 2862], ['ood', 6996]], 'labels': [1, 3, 5, 6, 9], 'scores': [0.6308453679084778, 0.5223985910415649, 0.8196090459823608, 0.7093361020088196, 0.5528266429901123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9010968208312988})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7085857391357422})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7703180313110352})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7828142642974854})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8935271501541138})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.65026767578125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 29592], ['id', 26266], ['id', 39673], ['id', 49094], ['id', 11304]], 'labels': [7, 7, 2, 5, 0], 'scores': [0.5832825303077698, 0.6403143405914307, 0.556915283203125, 0.700998067855835, 0.8225626945495605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8706986904144287})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7308201789855957})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7605001926422119})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8746773600578308})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8298500180244446})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8915, 'crossentropy': 0.6545421875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 52097], ['id', 28915], ['id', 44736], ['id', 12787], ['id', 7168]], 'labels': [1, 8, 5, 9, 8], 'scores': [0.5973142981529236, 0.4825887680053711, 0.8696849346160889, 0.658578097820282, 0.8801851272583008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9275308847427368})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.714195728302002})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.782970666885376})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8636051416397095})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8811112642288208})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8912, 'crossentropy': 0.66031923828125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 41923], ['id', 54769], ['id', 41982], ['id', 49121], ['id', 45658]], 'labels': [4, 4, 9, 9, 3], 'scores': [0.7358463406562805, 0.6743080615997314, 0.589907169342041, 0.7539607286453247, 0.5581735372543335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.817078709602356})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7296063899993896})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8145939111709595})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7945026159286499})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8000287413597107})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8929, 'crossentropy': 0.63226357421875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 40547], ['id', 16022], ['id', 47324], ['id', 22597], ['id', 57901]], 'labels': [8, 8, 0, 9, 8], 'scores': [0.7389408349990845, 0.8469060063362122, 0.5400257706642151, 0.5348561406135559, 0.5192058086395264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8200234174728394})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.673346221446991})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6409720182418823})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6855902671813965})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7705830335617065})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7495000958442688})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.571854443359375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 36839], ['id', 20169], ['id', 25910], ['id', 18031], ['id', 16843]], 'labels': [5, 4, 1, 4, 7], 'scores': [0.6197008490562439, 0.7643202543258667, 0.7503175735473633, 0.5929735898971558, 0.7873331904411316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8341633677482605})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7200356721878052})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7388473749160767})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7464090585708618})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8070321083068848})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8988, 'crossentropy': 0.61701708984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 47020], ['id', 58543], ['id', 11645], ['id', 9068], ['id', 27101]], 'labels': [5, 8, 3, 6, 6], 'scores': [0.5575568079948425, 0.5132040977478027, 0.6031613945960999, 0.5365414023399353, 0.6455199122428894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8603307008743286})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.643717885017395})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7528316974639893})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6903589963912964})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7351306676864624})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.551506396484375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 19423], ['id', 52121], ['id', 44123], ['id', 56191], ['id', 20745]], 'labels': [2, 5, 8, 3, 6], 'scores': [0.5889890193939209, 0.5884566307067871, 0.6525421142578125, 0.6595715880393982, 0.6100814342498779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9140737056732178})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6596160531044006})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5982882976531982})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6549681425094604})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6795585751533508})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7224702835083008})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.550643115234375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 20170], ['ood', 31965], ['id', 46615], ['ood', 16180], ['id', 47597]], 'labels': [9, 7, 7, 7, 8], 'scores': [0.7212110757827759, 0.5646019577980042, 0.7086508274078369, 0.592976987361908, 0.731690526008606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7643985748291016})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5837070941925049})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.593309760093689})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6222254037857056})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6317221522331238})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.52992744140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 58892], ['id', 34524], ['id', 14074], ['id', 15671], ['id', 19396]], 'labels': [3, 8, 5, 7, 5], 'scores': [0.5909819602966309, 0.6761139035224915, 0.5987604260444641, 0.4238472878932953, 0.4330235719680786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8693504333496094})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6343961358070374})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6238385438919067})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5701384544372559})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6075010299682617})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6110699772834778})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6598032116889954})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.52779228515625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 18150], ['id', 17231], ['id', 33505], ['id', 33057], ['id', 29542]], 'labels': [8, 4, 2, 7, 4], 'scores': [0.9321693181991577, 0.8471778035163879, 0.9510998129844666, 1.0073217749595642, 0.6772155165672302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8689759969711304})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.611994206905365})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5389721393585205})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5991425514221191})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5444948077201843})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5523606538772583})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.52005078125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 39421], ['id', 40221], ['id', 31512], ['id', 34650], ['id', 57307]], 'labels': [2, 2, 2, 2, 2], 'scores': [0.7889754772186279, 0.7922529578208923, 0.9917424917221069, 1.0423068404197693, 0.9100124835968018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9526298642158508})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6267966628074646})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5207499265670776})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5599437952041626})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6279729604721069})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5758613348007202})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.456702294921875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 57812], ['id', 38391], ['id', 47234], ['id', 42153], ['id', 9241]], 'labels': [5, 8, 1, 0, 8], 'scores': [0.5548023879528046, 0.7085386514663696, 0.6507610082626343, 0.4930187463760376, 0.5732884407043457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8309566974639893})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5975123643875122})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.519677996635437})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5209705233573914})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5680299997329712})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.538149356842041})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.48529658203125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 18003], ['id', 14604], ['id', 33709], ['id', 57728], ['id', 23505]], 'labels': [2, 6, 3, 9, 1], 'scores': [0.8434500694274902, 0.4985467791557312, 0.6598674654960632, 0.8371714949607849, 0.484478235244751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8266881704330444})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5860154628753662})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5233174562454224})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5331852436065674})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5284932851791382})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5545090436935425})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.521821875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 25783], ['id', 52940], ['id', 12067], ['id', 13337], ['id', 53019]], 'labels': [0, 3, 7, 7, 2], 'scores': [0.6650025844573975, 0.6658531427383423, 0.506832480430603, 0.7813950777053833, 0.8600406646728516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8720295429229736})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5001131296157837})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4689819812774658})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4845588207244873})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5019214749336243})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49712514877319336})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.46235791015625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8698], ['id', 51241], ['ood', 13652], ['id', 30907], ['id', 12179]], 'labels': [7, 2, 0, 3, 9], 'scores': [0.6554096341133118, 0.49138665199279785, 0.30041539669036865, 0.617908239364624, 0.7066143155097961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8530179858207703})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5618436336517334})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.477711021900177})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4828600287437439})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4501776695251465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45854273438453674})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46334308385849})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4895235300064087})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.4247103515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 35803], ['id', 31482], ['id', 18682], ['id', 55906], ['id', 20903]], 'labels': [5, 3, 7, 2, 3], 'scores': [0.5087071657180786, 0.8562844395637512, 0.5126283764839172, 0.6738337874412537, 0.7961391806602478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8423076868057251})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4839722514152527})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4621778130531311})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4798046946525574})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4640277922153473})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40531450510025024})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4682764708995819})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4729853868484497})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.627565324306488})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.422131689453125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 8171], ['id', 21532], ['id', 32646], ['id', 59314], ['id', 31988]], 'labels': [8, 5, 5, 9, 3], 'scores': [0.6652023792266846, 0.6281439065933228, 0.5205568671226501, 0.928885817527771, 0.6108144521713257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8095712661743164})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4952644109725952})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4580174684524536})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4565027356147766})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.455471396446228})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.460326611995697})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4529927372932434})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5115142464637756})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4659261107444763})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4414522051811218})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4743919372558594})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4588698446750641})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4903585910797119})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.418969384765625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 22670], ['id', 3942], ['id', 37116], ['id', 16860], ['id', 1004]], 'labels': [4, 7, 1, 8, 4], 'scores': [0.48330968618392944, 0.6152359247207642, 0.7874762415885925, 0.9697757959365845, 0.7353969812393188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9197076559066772})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5776004791259766})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41525986790657043})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46113619208335876})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.43742209672927856})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4433332085609436})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.938, 'crossentropy': 0.4173740234375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 56454], ['id', 8771], ['id', 33162], ['id', 27337], ['id', 22750]], 'labels': [0, 3, 8, 5, 4], 'scores': [0.7487325668334961, 0.6521896719932556, 0.6254109740257263, 0.6589942574501038, 0.5906449556350708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0580687522888184})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5519506931304932})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4503459334373474})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47188055515289307})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4569381773471832})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4465565085411072})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4521327614784241})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5107670426368713})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5222227573394775})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.416697265625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 51277], ['id', 54275], ['id', 52462], ['id', 47076], ['id', 47540]], 'labels': [1, 9, 9, 8, 9], 'scores': [0.42088568210601807, 0.6111970245838165, 0.7026470303535461, 0.8575038909912109, 0.8837354779243469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9049311876296997})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5247381925582886})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4653714895248413})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4685000777244568})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.443083792924881})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4502650499343872})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42953765392303467})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4877201318740845})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4699397683143616})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4569089710712433})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.3841994873046875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52358], ['id', 18473], ['id', 42828], ['id', 18440], ['id', 29723]], 'labels': [2, 4, 7, 5, 5], 'scores': [0.6842647790908813, 0.7487508654594421, 0.8472239375114441, 0.3361344635486603, 0.849738597869873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0007480382919312})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5891029834747314})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43234628438949585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4158362150192261})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45786017179489136})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43440407514572144})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4374547600746155})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.3996794189453125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 29719], ['id', 47297], ['id', 27930], ['id', 40208], ['id', 6246]], 'labels': [3, 8, 3, 0, 6], 'scores': [0.6214065551757812, 0.7397994995117188, 0.7875945866107941, 0.6131110191345215, 0.6321448087692261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8593918085098267})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.487962543964386})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45540791749954224})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4263693690299988})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4704177975654602})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4574636220932007})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4526025652885437})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9454, 'crossentropy': 0.38039052734375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 45593], ['id', 29365], ['id', 16756], ['id', 18739], ['id', 49589]], 'labels': [6, 8, 7, 3, 3], 'scores': [0.5996255278587341, 0.6570706367492676, 0.7029719352722168, 0.6188919544219971, 0.8165634274482727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9148539304733276})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5274918079376221})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.457332968711853})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43665122985839844})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4450351595878601})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4353695511817932})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4293595254421234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45623502135276794})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4805206060409546})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4324868321418762})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.3787424072265625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 57345], ['id', 20578], ['id', 23350], ['id', 52744], ['id', 46379]], 'labels': [5, 8, 8, 7, 3], 'scores': [0.7082446217536926, 0.7891627550125122, 0.8162629008293152, 0.7268593907356262, 0.7804107069969177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0200257301330566})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.501036524772644})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41874656081199646})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4398486912250519})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40261924266815186})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39897364377975464})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40057510137557983})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3817325234413147})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40921348333358765})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4506160020828247})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4350869059562683})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.3591192626953125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 23546], ['id', 27964], ['id', 4812], ['id', 43176], ['id', 46654]], 'labels': [5, 8, 4, 2, 0], 'scores': [0.9604540467262268, 0.738421618938446, 0.48408937454223633, 0.6976889371871948, 0.719049334526062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9915133118629456})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.475460410118103})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.448067843914032})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3870643973350525})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40597787499427795})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37570634484291077})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41426244378089905})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3926334083080292})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42091524600982666})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9525, 'crossentropy': 0.3387701904296875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 52331], ['id', 38688], ['id', 10038], ['id', 56300], ['id', 57054]], 'labels': [2, 7, 9, 9, 8], 'scores': [0.45853734016418457, 0.75751131772995, 0.7796392440795898, 0.61712646484375, 0.6255865693092346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8543896079063416})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.458368718624115})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38262367248535156})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35697227716445923})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37798893451690674})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3866350054740906})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3870004415512085})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.3300307373046875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 47496], ['id', 14749], ['id', 35736], ['id', 45062], ['id', 13030]], 'labels': [3, 0, 6, 9, 0], 'scores': [0.6551500558853149, 0.8867476582527161, 0.5354862213134766, 0.726659893989563, 0.9098047614097595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.955530047416687})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46417391300201416})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4266681969165802})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3938175439834595})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37432658672332764})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3802497088909149})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4135964512825012})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4039137363433838})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.355758447265625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 39778], ['id', 9036], ['id', 45784], ['id', 26477], ['id', 2208]], 'labels': [8, 2, 9, 2, 4], 'scores': [0.873802661895752, 0.6344338059425354, 0.9312299489974976, 0.5906113982200623, 0.5587339997291565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8922785520553589})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4795650839805603})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39877793192863464})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41636860370635986})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4477982521057129})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3723163604736328})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3880118727684021})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42240095138549805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41619640588760376})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9497, 'crossentropy': 0.3700569580078125}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 53054], ['id', 13709], ['id', 33101], ['ood', 48824], ['ood', 55629]], 'labels': [2, 6, 8, 5, 5], 'scores': [0.6787096261978149, 0.8163435459136963, 0.6462552845478058, 0.43609023094177246, 0.538673996925354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.047853946685791})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5451937317848206})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4497048854827881})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40956053137779236})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3887624740600586})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40295761823654175})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4167368710041046})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41840237379074097})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3589865966796875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 13192], ['id', 14881], ['id', 13996], ['id', 19590], ['id', 30177]], 'labels': [7, 2, 9, 5, 7], 'scores': [0.5707747936248779, 0.7389302253723145, 0.7585647106170654, 0.7496828436851501, 0.5709216594696045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0845195055007935})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5639575719833374})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43180322647094727})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.414524644613266})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3845983147621155})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42378535866737366})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35422980785369873})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4255833625793457})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35385650396347046})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3754788935184479})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3996508717536926})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45540791749954224})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.957, 'crossentropy': 0.328713720703125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 43212], ['id', 29751], ['id', 9966], ['id', 30959], ['id', 7056]], 'labels': [5, 8, 0, 7, 9], 'scores': [0.79376220703125, 0.729584813117981, 0.8998441696166992, 0.6051579117774963, 0.5305452346801758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.216789722442627})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5845466256141663})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40251365303993225})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4303058981895447})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3996032476425171})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37868785858154297})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3601643741130829})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3928859829902649})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3829658329486847})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3912743330001831})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.325717333984375}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 38209], ['id', 43056], ['id', 32766], ['id', 6962], ['id', 29002]], 'labels': [1, 5, 8, 8, 7], 'scores': [0.27103424072265625, 0.6094734072685242, 0.7034380435943604, 0.7186324596405029, 0.8067607879638672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9729536771774292})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.507841944694519})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4241982102394104})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40011823177337646})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3617534637451172})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3235715627670288})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3559991717338562})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3817339241504669})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36333370208740234})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.32309287109375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 42180], ['id', 46736], ['id', 38698], ['id', 35326], ['id', 34396]], 'labels': [0, 3, 5, 5, 3], 'scores': [0.7818411588668823, 0.5610888600349426, 0.824914813041687, 0.8048636317253113, 0.6304330825805664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.023284673690796})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5635055303573608})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4096120595932007})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38383936882019043})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3522788882255554})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3446865975856781})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3725997805595398})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3448609709739685})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35751837491989136})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.30532158203125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 15191], ['id', 24998], ['id', 17292], ['id', 8693], ['id', 14394]], 'labels': [0, 9, 3, 3, 3], 'scores': [0.7380907535552979, 0.8079099357128143, 0.603874921798706, 0.8587586283683777, 0.929423987865448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0476089715957642})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5562093257904053})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4540685713291168})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4214748740196228})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3870590329170227})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35660606622695923})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36458635330200195})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40099507570266724})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3692835867404938})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.3356373291015625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 2782], ['id', 56379], ['id', 53638], ['id', 56328], ['id', 49563]], 'labels': [8, 4, 5, 1, 8], 'scores': [0.420448899269104, 0.5638817548751831, 0.6233884692192078, 0.3545110821723938, 0.7959387302398682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1272410154342651})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5267001986503601})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45717310905456543})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4056835174560547})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39616164565086365})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41623470187187195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38171303272247314})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3873023986816406})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39628422260284424})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4298466444015503})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9566, 'crossentropy': 0.337594775390625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 24312], ['id', 45602], ['id', 28212], ['id', 35246], ['id', 49506]], 'labels': [8, 5, 2, 8, 9], 'scores': [0.6644121408462524, 0.7369978427886963, 0.7803604006767273, 0.8282384872436523, 0.5625036954879761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2451233863830566})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6502985954284668})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4405047297477722})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38635051250457764})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.390430212020874})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41221338510513306})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40855270624160767})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9566, 'crossentropy': 0.356972021484375}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 35503], ['id', 28362], ['id', 6374], ['id', 46423], ['id', 8678]], 'labels': [9, 7, 5, 9, 1], 'scores': [0.5959028601646423, 0.6351364254951477, 0.34329360723495483, 0.5008364319801331, 0.8014585375785828]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0028823614120483})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.512702226638794})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43992704153060913})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38894397020339966})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3574727177619934})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3823917508125305})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39663293957710266})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.345248281955719})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3835059404373169})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.407853901386261})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40313565731048584})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3186201416015625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 13215], ['id', 50878], ['id', 47100], ['id', 34765], ['id', 32048]], 'labels': [0, 7, 8, 6, 7], 'scores': [0.7544663548469543, 0.8221424221992493, 0.7958073616027832, 1.0579439401626587, 0.7588466703891754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1571118831634521})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5659716129302979})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4370417594909668})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39030027389526367})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34711456298828125})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3404587209224701})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.360278844833374})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38726091384887695})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35062915086746216})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.2883463134765625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 2258], ['id', 38315], ['ood', 55778], ['id', 39948], ['id', 3692]], 'labels': [5, 0, 8, 8, 7], 'scores': [0.6978744864463806, 0.701892614364624, 0.5085784196853638, 0.45372188091278076, 0.7995566725730896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3129496574401855})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6060159206390381})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.501693844795227})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41637057065963745})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3944079875946045})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4080140292644501})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35771965980529785})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39398008584976196})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3756680488586426})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3782173991203308})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.307426220703125}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 13827], ['ood', 18669], ['id', 1243], ['id', 17820], ['id', 19302]], 'labels': [3, 5, 1, 3, 3], 'scores': [0.6216177344322205, 0.5645164251327515, 0.6196461319923401, 0.48218029737472534, 0.7179431915283203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.133680820465088})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5491498708724976})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41094809770584106})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3693613111972809})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38530099391937256})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3650796711444855})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35724782943725586})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3617514371871948})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35644856095314026})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37473028898239136})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3730618953704834})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39375758171081543})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.293334130859375}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 27877], ['id', 31413], ['id', 14290], ['id', 54782], ['id', 17698]], 'labels': [5, 5, 4, 3, 9], 'scores': [0.6152891516685486, 0.912646472454071, 0.5872920155525208, 0.7804679870605469, 0.7917476296424866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1152262687683105})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5157643556594849})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4231914281845093})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34947410225868225})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31389325857162476})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3175092041492462})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3242676258087158})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3401607871055603})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.31911103515625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 59126], ['id', 44100], ['id', 11403], ['id', 41020], ['id', 39668]], 'labels': [4, 4, 0, 4, 8], 'scores': [0.5475131869316101, 0.6535894870758057, 0.7330465316772461, 0.6083979606628418, 0.6752067804336548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.3514366149902344})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5924115777015686})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4791877865791321})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3659437596797943})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33991312980651855})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36485350131988525})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33780139684677124})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3344688415527344})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36318981647491455})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3567175269126892})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31786713004112244})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3216768801212311})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3618276119232178})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3548535108566284})
store['active_learning_steps'][56]['training']['best_epoch']=11
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.290720166015625}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 55314], ['id', 49464], ['id', 24485], ['id', 27968], ['id', 45012]], 'labels': [6, 9, 2, 9, 5], 'scores': [0.7025156617164612, 0.7549311518669128, 0.6321612596511841, 0.6478320956230164, 0.9845145344734192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.009948968887329})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5848797559738159})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38617992401123047})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36579012870788574})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34961819648742676})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32012128829956055})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3267172574996948})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31226834654808044})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3273564279079437})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32800209522247314})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37310874462127686})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2652434814453125}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 54777], ['id', 28371], ['id', 19089], ['id', 54878], ['id', 7229]], 'labels': [4, 3, 5, 4, 7], 'scores': [0.3613787293434143, 0.8964195251464844, 0.6109322011470795, 0.6875410676002502, 0.5953884720802307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1572721004486084})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6036856174468994})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4028165936470032})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3582306504249573})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32127630710601807})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31090694665908813})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27771884202957153})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3232558071613312})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3106335997581482})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29804545640945435})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2478967041015625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 12938], ['id', 55268], ['id', 13428], ['id', 8721], ['id', 49505]], 'labels': [2, 8, 9, 9, 6], 'scores': [0.4828920066356659, 0.983931303024292, 0.6989142894744873, 0.6741358041763306, 0.6207029819488525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0012189149856567})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5100606679916382})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3908384442329407})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41557425260543823})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32929182052612305})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3422589898109436})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.318508505821228})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3311071991920471})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3183031380176544})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2991851568222046})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31728699803352356})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3239057958126068})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3526756763458252})
store['active_learning_steps'][59]['training']['best_epoch']=10
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.27181943359375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 45422], ['id', 41453], ['id', 31554], ['id', 30139], ['ood', 59696]], 'labels': [0, 3, 5, 6, 0], 'scores': [0.9526330828666687, 0.6660493612289429, 0.640002965927124, 0.8558179140090942, 0.30243921279907227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1894173622131348})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.579785943031311})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44151535630226135})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.358137845993042})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32663393020629883})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3612055778503418})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31014350056648254})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32776516675949097})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36301320791244507})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3509519398212433})
store['active_learning_steps'][60]['training']['best_epoch']=7
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.291618505859375}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 21369], ['id', 53978], ['id', 19130], ['id', 1758], ['id', 16692]], 'labels': [9, 5, 5, 8, 5], 'scores': [0.6323536038398743, 1.0053284764289856, 0.43895283341407776, 0.6133697032928467, 0.8885231614112854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.208841323852539})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5358453392982483})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44692084193229675})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3436128497123718})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3384150564670563})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3104793429374695})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3230142891407013})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29475095868110657})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31104886531829834})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2905260920524597})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3044096827507019})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3108322024345398})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3175716698169708})
store['active_learning_steps'][61]['training']['best_epoch']=10
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.27175078125}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 24193], ['id', 50371], ['id', 55066], ['id', 27118], ['ood', 36985]], 'labels': [9, 7, 6, 8, 5], 'scores': [0.5524013638496399, 0.7647958397865295, 0.40729230642318726, 0.7513577342033386, 0.3917194604873657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0436069965362549})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5187822580337524})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3777681887149811})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35670000314712524})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31251347064971924})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3265593647956848})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3397254943847656})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.324840784072876})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.26534501953125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 16672], ['ood', 51242], ['id', 5679], ['id', 26850], ['id', 29410]], 'labels': [7, 9, 3, 2, 5], 'scores': [0.48217064142227173, 0.3091672658920288, 0.7541434168815613, 0.5702183842658997, 0.6364365816116333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.2386338710784912})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.64555823802948})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44754743576049805})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3459874391555786})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3490784168243408})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3195228576660156})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29090404510498047})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3153296113014221})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33729639649391174})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32721513509750366})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2582598876953125}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 50618], ['id', 3072], ['id', 47093], ['id', 16755], ['id', 36908]], 'labels': [6, 4, 8, 3, 1], 'scores': [0.7289336919784546, 0.7276558876037598, 0.7227500081062317, 0.82440185546875, 0.8200768828392029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2659245729446411})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5716822743415833})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42602503299713135})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3242483139038086})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2960093021392822})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29601776599884033})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28384169936180115})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2794363498687744})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2812206745147705})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30788886547088623})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2854989767074585})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.266197314453125}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 45649], ['id', 20918], ['id', 49517], ['id', 34829], ['id', 1674]], 'labels': [8, 9, 6, 5, 9], 'scores': [0.4176514744758606, 0.7397842407226562, 0.882305920124054, 0.7100951671600342, 0.9431245923042297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1051312685012817})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5429835319519043})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4144604206085205})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3609536290168762})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2876199185848236})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.292510449886322})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2864672541618347})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3323003053665161})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2869721055030823})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26242366433143616})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2861520051956177})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3184077739715576})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.306882381439209})
store['active_learning_steps'][65]['training']['best_epoch']=10
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.250287841796875}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 3355], ['id', 12305], ['id', 44948], ['id', 42233], ['id', 22910]], 'labels': [9, 9, 9, 4, 0], 'scores': [0.655683308839798, 0.9433639049530029, 0.7270392775535583, 0.6450842916965485, 0.4696105718612671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1978936195373535})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6277104616165161})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40939033031463623})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35984063148498535})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2894274592399597})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2975313067436218})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33615148067474365})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2961786091327667})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2916052734375}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 19524], ['id', 49416], ['id', 3538], ['id', 27490], ['id', 2843]], 'labels': [2, 2, 7, 2, 1], 'scores': [0.7181708216667175, 0.5224894881248474, 0.4319245219230652, 0.5802991390228271, 0.5665497779846191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0198121070861816})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46731942892074585})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3285839557647705})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3284309506416321})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30527573823928833})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2644974887371063})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24805909395217896})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2613556385040283})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26559966802597046})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25689613819122314})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.23420517578125}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 36270], ['id', 50316], ['id', 14728], ['id', 11708], ['id', 148]], 'labels': [8, 5, 8, 3, 7], 'scores': [0.5276769995689392, 0.6539097726345062, 0.5715456008911133, 0.7553748488426208, 0.5410099625587463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1048510074615479})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5850028991699219})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38568544387817383})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3612022399902344})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3386140465736389})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3170526921749115})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2896023094654083})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2823614180088043})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3016452193260193})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29579776525497437})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3044722080230713})
store['active_learning_steps'][68]['training']['best_epoch']=8
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2825539794921875}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 39329], ['id', 39734], ['id', 17494], ['id', 18608], ['id', 21174]], 'labels': [3, 2, 5, 6, 2], 'scores': [0.564498782157898, 0.4845982789993286, 0.8151181936264038, 0.5641288757324219, 0.6302457451820374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3131506443023682})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5957950353622437})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4233090281486511})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35499751567840576})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34174591302871704})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3229272663593292})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3274046778678894})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2991698384284973})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3479999601840973})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31008103489875793})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30108442902565})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.247564501953125}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 42616], ['id', 31845], ['id', 19630], ['id', 51396], ['id', 3508]], 'labels': [4, 8, 1, 4, 9], 'scores': [0.5115267038345337, 0.8226967453956604, 0.5152162909507751, 0.3112947940826416, 0.6703765392303467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1701308488845825})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6416991353034973})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3941476345062256})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3580455780029297})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3466064929962158})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3176184296607971})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3181956112384796})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29747989773750305})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32074519991874695})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3454883098602295})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33394670486450195})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.255980712890625}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 36818], ['id', 21576], ['id', 6347], ['id', 32396], ['id', 2184]], 'labels': [7, 0, 3, 9, 2], 'scores': [0.8842710852622986, 0.7374350428581238, 0.9614670276641846, 0.6758300364017487, 0.6537993848323822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1454777717590332})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6215198040008545})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42342448234558105})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3406774401664734})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3186100721359253})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3324907422065735})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2796761989593506})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2959253787994385})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29696765542030334})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3126007318496704})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.242743505859375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 15781], ['id', 37676], ['id', 3644], ['id', 15870], ['id', 47910]], 'labels': [5, 6, 1, 6, 1], 'scores': [0.695103645324707, 0.4945828914642334, 0.6155280470848083, 0.5121888518333435, 0.5686230957508087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.037168025970459})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5282478332519531})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3785543441772461})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3259912133216858})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2997828423976898})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30499404668807983})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28860217332839966})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.268954873085022})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2939310073852539})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2637050151824951})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2520817816257477})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2894350290298462})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28948357701301575})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3023952543735504})
store['active_learning_steps'][72]['training']['best_epoch']=11
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.239781494140625}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 36446], ['id', 3268], ['id', 42933], ['id', 57686], ['id', 13911]], 'labels': [6, 6, 4, 0, 0], 'scores': [0.9015940427780151, 0.7546939253807068, 0.8653659224510193, 0.5437559187412262, 0.49106624722480774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.271502137184143})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5321559906005859})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39373522996902466})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3573845624923706})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31554698944091797})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31687235832214355})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3039560914039612})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2954464852809906})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29894617199897766})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28745317459106445})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29433301091194153})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2870146930217743})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.306270956993103})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30746814608573914})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28683215379714966})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2868477702140808})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3305135667324066})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3113081455230713})
store['active_learning_steps'][73]['training']['best_epoch']=15
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.246446533203125}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 5723], ['id', 45939], ['id', 43636], ['id', 32328], ['id', 43686]], 'labels': [7, 0, 4, 4, 7], 'scores': [0.6004046201705933, 0.7306548953056335, 0.9372265934944153, 0.6701485514640808, 0.7396584749221802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2020206451416016})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4947580099105835})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35737770795822144})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33294716477394104})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.299977570772171})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27000924944877625})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25619906187057495})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30247944593429565})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2817540168762207})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27320459485054016})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2361363525390625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 27429], ['id', 8104], ['id', 20792], ['id', 5103], ['id', 11734]], 'labels': [0, 5, 9, 2, 8], 'scores': [0.7793182730674744, 0.7742197513580322, 0.690845787525177, 0.79410719871521, 0.5885733366012573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2414438724517822})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5601507425308228})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3689398169517517})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3089783191680908})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29122185707092285})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28457266092300415})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2479007989168167})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2590930163860321})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2618560194969177})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.251321405172348})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.238680419921875}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 16853], ['id', 10301], ['id', 58777], ['id', 25546], ['id', 38246]], 'labels': [9, 1, 8, 8, 7], 'scores': [0.5279385447502136, 0.6189804077148438, 0.6935176849365234, 0.6114538908004761, 0.5789952874183655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2190465927124023})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6623469591140747})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4346177577972412})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.355013906955719})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.307259202003479})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2810801863670349})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.282731294631958})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27104097604751587})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26954883337020874})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26205241680145264})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24786865711212158})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22369596362113953})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26491737365722656})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2712487578392029})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26862695813179016})
store['active_learning_steps'][76]['training']['best_epoch']=12
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9756, 'crossentropy': 0.2344054443359375}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 26405], ['id', 854], ['id', 47479], ['id', 26206], ['id', 41424]], 'labels': [9, 2, 0, 5, 1], 'scores': [0.9738687872886658, 0.7706544995307922, 0.7726456522941589, 0.8609032034873962, 0.7248533368110657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1793551445007324})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4830981492996216})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3758597671985626})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31519919633865356})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30286282300949097})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26724594831466675})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27435213327407837})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2674516439437866})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28643128275871277})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.24349482421875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 2980], ['id', 15276], ['ood', 29091], ['id', 34740], ['id', 19942]], 'labels': [7, 7, 1, 3, 5], 'scores': [0.5642671585083008, 0.6814808249473572, 0.23660194873809814, 0.6301935911178589, 0.7070056200027466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1166999340057373})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5890883803367615})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4025821387767792})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3030930757522583})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2894045412540436})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2976844906806946})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29714423418045044})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28364089131355286})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2693343758583069})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2980458736419678})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2839444875717163})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2760199308395386})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.230084814453125}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 48006], ['id', 3510], ['id', 20110], ['id', 15412], ['id', 1423]], 'labels': [6, 9, 4, 3, 0], 'scores': [0.7603251934051514, 0.5108956098556519, 0.7339675426483154, 0.7534447312355042, 0.777299165725708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.122753381729126})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5602421760559082})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38516777753829956})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.308216392993927})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31682872772216797})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2651623487472534})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25751352310180664})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26298025250434875})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2656998038291931})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2752249836921692})
store['active_learning_steps'][79]['training']['best_epoch']=7
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2352738525390625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 51799], ['id', 19832], ['id', 2064], ['id', 30742], ['id', 5216]], 'labels': [3, 9, 7, 1, 2], 'scores': [0.5918073058128357, 0.5313717722892761, 0.7281615734100342, 0.508480429649353, 0.8197675347328186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1800181865692139})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.556199312210083})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4191557765007019})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3238111734390259})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29167211055755615})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2910759747028351})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26005107164382935})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29265642166137695})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27220988273620605})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2698422074317932})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.24694482421875}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 25116], ['id', 44961], ['id', 40046], ['id', 5155], ['id', 52727]], 'labels': [3, 8, 7, 4, 4], 'scores': [0.5876432657241821, 0.7711082696914673, 0.5220812857151031, 0.8245763778686523, 0.3263123035430908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1853845119476318})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5891485810279846})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3758277893066406})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3457682728767395})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3063247501850128})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30726468563079834})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2844114899635315})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.267518013715744})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3022444248199463})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2907145321369171})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2953953444957733})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2264119873046875}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 48726], ['id', 35482], ['id', 58832], ['id', 59294], ['id', 37118]], 'labels': [8, 4, 3, 8, 3], 'scores': [0.8001056909561157, 0.6250180006027222, 0.7673760652542114, 0.6955984830856323, 0.5694871544837952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2617170810699463})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6179003119468689})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4016795754432678})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3105786442756653})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3086793124675751})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29438191652297974})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27296993136405945})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26579493284225464})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24652917683124542})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24497175216674805})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26573264598846436})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27629774808883667})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27562007308006287})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9769, 'crossentropy': 0.2157153564453125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 31301], ['id', 43174], ['id', 40654], ['id', 31252], ['id', 8940]], 'labels': [5, 9, 5, 5, 6], 'scores': [0.9705538749694824, 0.8426626324653625, 0.759249210357666, 0.7285621762275696, 0.7312947511672974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.250152826309204})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5772864818572998})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4339485764503479})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3301461338996887})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2796429991722107})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24834182858467102})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26401522755622864})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27253076434135437})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23947983980178833})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23926305770874023})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25089120864868164})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2471725344657898})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2346826195716858})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24010568857192993})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22524049878120422})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2620258629322052})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28808730840682983})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.251983642578125})
store['active_learning_steps'][83]['training']['best_epoch']=15
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9777, 'crossentropy': 0.206647705078125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 37758], ['id', 33137], ['id', 5163], ['id', 31044], ['id', 34707]], 'labels': [0, 5, 8, 3, 8], 'scores': [0.8389366865158081, 0.44422245025634766, 0.9086290299892426, 0.7118446826934814, 0.8260534405708313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2274582386016846})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6728947162628174})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43870776891708374})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.36726897954940796})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2775861620903015})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3114030361175537})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29305583238601685})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2794288694858551})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2904743408203125}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 46122], ['id', 22149], ['id', 10032], ['id', 35430], ['id', 59297]], 'labels': [2, 3, 6, 1, 1], 'scores': [0.6161597371101379, 0.4478374123573303, 0.6732562184333801, 0.3480300307273865, 0.6347205638885498]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.164853811264038})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6114928722381592})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4173271656036377})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3391287326812744})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3254629969596863})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2669043242931366})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25169509649276733})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2824249267578125})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25464165210723877})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24799351394176483})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2687491476535797})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2816866636276245})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2474687695503235})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26387259364128113})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25406700372695923})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2723359763622284})
store['active_learning_steps'][85]['training']['best_epoch']=13
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9753, 'crossentropy': 0.229443017578125}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 40466], ['id', 13760], ['id', 3941], ['id', 15528], ['id', 788]], 'labels': [8, 6, 3, 5, 9], 'scores': [0.749710202217102, 0.7324459552764893, 0.6256427764892578, 0.645397961139679, 0.8810001015663147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1808217763900757})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5479505062103271})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40852445363998413})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34454578161239624})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29762911796569824})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2453409880399704})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.262065589427948})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25491657853126526})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2663000822067261})
store['active_learning_steps'][86]['training']['best_epoch']=6
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9747, 'crossentropy': 0.2445983154296875}
