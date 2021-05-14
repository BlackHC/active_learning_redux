store = {}
store['timestamp']=1620917057
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=18']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=20
store['config']={'seed': 1261, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2005574703216553})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4250848293304443})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.841845989227295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6365866661071777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 2.0028982421875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1182928085327148})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0871222019195557})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.075007677078247})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [12337, 32022, 58577, 11071, 52482, 34905, 48210, 54481, 44101, 40467], 'labels': [0, 2, 9, 0, 6, 6, 0, 3, 3, 8], 'scores': [0.9259961247444153, 0.8405023217201233, 0.6887810826301575, 0.9876839518547058, 0.6222878694534302, 0.8161138892173767, 0.8866011500358582, 0.9437252283096313, 0.9396372437477112, 1.0833536982536316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8379919528961182})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9642221927642822})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4851551055908203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.4807255268096924})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6929, 'crossentropy': 1.7044546875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1645818948745728})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1134679317474365})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1072776317596436})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [46269, 17609, 52945, 34947, 37397, 50013, 4114, 34150, 23112, 27125], 'labels': [3, 8, 4, 4, 3, 8, 4, 8, 8, 4], 'scores': [0.5322479009628296, 0.5890449285507202, 0.7401509284973145, 0.743680477142334, 0.615106463432312, 0.6278381943702698, 0.697346568107605, 0.675471305847168, 0.6478404402732849, 0.6193166971206665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7416993379592896})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.0484890937805176})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.189136028289795})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.3941564559936523})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7162, 'crossentropy': 1.6185193359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0898789167404175})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0711441040039062})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.058833122253418})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [11439, 12082, 36609, 47450, 45791, 4692, 7644, 25798, 32711, 48637], 'labels': [1, 5, 5, 6, 3, 8, 7, 6, 5, -1], 'scores': [0.4351769685745239, 0.5816934108734131, 0.5910908579826355, 0.5301477909088135, 0.46927547454833984, 0.723275363445282, 0.621045708656311, 0.64634770154953, 0.47806882858276367, 0.44958364963531494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.487697720527649})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6231940984725952})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.0718517303466797})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.9353256225585938})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.781, 'crossentropy': 1.3234361328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0054118633270264})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9621666669845581})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.8693501949310303})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [43547, 22648, 24786, 25883, 16948, 28040, 26588, 15421, 31103, 58437], 'labels': [2, 9, 2, 3, 2, 5, 4, 5, 8, 9], 'scores': [0.6353549361228943, 0.5694384574890137, 0.514772355556488, 0.5379891395568848, 0.6672114729881287, 0.6814279556274414, 0.661952018737793, 0.35623013973236084, 0.6127145290374756, 0.6459704041481018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3853521347045898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.543244481086731})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6853320598602295})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 2.0600109100341797})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8091, 'crossentropy': 1.195136328125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9725916385650635})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9141936898231506})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8551391363143921})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [48064, 19755, 38970, 41370, 25356, 49578, 39611, 33425, 41919, 29423], 'labels': [3, 2, 3, 5, 5, 8, 8, 1, 7, 7], 'scores': [0.6244403123855591, 0.49506568908691406, 0.6614718437194824, 0.615216851234436, 0.34375709295272827, 0.2952357530593872, 0.6092156767845154, 0.6397519111633301, 0.6198981404304504, 0.510346531867981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0010539293289185})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1954662799835205})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.179565191268921})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3501293659210205})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8513, 'crossentropy': 0.84020966796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8813445568084717})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7607705593109131})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7270524501800537})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [59339, 56127, 54989, 27120, 36007, 28326, 17989, 5649, 21375, 56067], 'labels': [1, 5, 9, 2, 9, -1, 9, 3, 8, 3], 'scores': [0.4944092631340027, 0.45697033405303955, 0.41072338819503784, 0.6734300851821899, 0.4268077611923218, 0.2587158679962158, 0.46086716651916504, 0.6120551824569702, 0.688737690448761, 0.6118062734603882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8862702250480652})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0570684671401978})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0556784868240356})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0881880521774292})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8554, 'crossentropy': 0.80033056640625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8070157766342163})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7208226919174194})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7113877534866333})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [39410, 10799, 39080, 2118, 41389, 36767, 27750, 39096, 18782, 12196], 'labels': [5, 9, 4, 7, 5, 7, 6, 9, 5, 2], 'scores': [0.4905257225036621, 0.4598046541213989, 0.45631396770477295, 0.3267973065376282, 0.3996286392211914, 0.3867452144622803, 0.4575462341308594, 0.5507057309150696, 0.49282050132751465, 0.4279637336730957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8194719552993774})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8157811164855957})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7612638473510742})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.913960337638855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9134014248847961})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8900984525680542})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.66714697265625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6930720806121826})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5674514174461365})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5425816774368286})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5387353301048279})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.47689759731292725})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [11829, 13713, 37437, 55208, 1088, 32387, 207, 11122, 18506, 32747], 'labels': [-1, 3, 2, -1, 7, 4, 3, 7, 9, 8], 'scores': [0.4327312707901001, 0.6491246223449707, 0.6414949297904968, 0.5857536792755127, 0.5170685052871704, 0.584073543548584, 0.6458666324615479, 0.7423922419548035, 0.6741137504577637, 0.7698958516120911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7644252777099609})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6836345195770264})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.717136800289154})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8073011040687561})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8688420057296753})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.572059326171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7078646421432495})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5915294289588928})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5361351370811462})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5011584162712097})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [18130, 5699, 50320, 6480, 45801, 30041, 12377, 11584, 25159, 31924], 'labels': [8, 8, 5, 2, 3, 3, 3, 0, 0, -1], 'scores': [0.2557745575904846, 0.32498329877853394, 0.5699687004089355, 0.4065784811973572, 0.35292303562164307, 0.500361442565918, 0.5738043785095215, 0.25830912590026855, 0.3537898659706116, 0.24730628728866577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8021354675292969})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6785006523132324})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6886943578720093})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.794098436832428})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7647891640663147})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.61335361328125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.690339982509613})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5929396152496338})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5295044183731079})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5264450907707214})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [14062, 32348, 53120, 15743, 3119, 11482, 38130, 34188, 41999, 37825], 'labels': [8, 5, 5, 3, 8, 8, 3, 3, 0, 2], 'scores': [0.49265289306640625, 0.5185925960540771, 0.5275624990463257, 0.4681798219680786, 0.27292948961257935, 0.4839046001434326, 0.6629772186279297, 0.5040103793144226, 0.46784234046936035, 0.40194177627563477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7972607612609863})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6441365480422974})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.719316840171814})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7710297703742981})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6644139289855957})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.560399658203125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.698935866355896})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5181176662445068})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4755443334579468})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4871516823768616})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [826, 35326, 23027, 31312, 14732, 37934, 57331, 49531, 49511, 48271], 'labels': [9, 5, -1, 9, 6, 9, 2, 7, 9, 7], 'scores': [0.6456412076950073, 0.5341130495071411, 0.33845919370651245, 0.5261940956115723, 0.4157062768936157, 0.46048200130462646, 0.38511353731155396, 0.34207361936569214, 0.47073793411254883, 0.4803866147994995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8356238603591919})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6315191388130188})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5780277252197266})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6948655843734741})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6642559766769409})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.726001501083374})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.5788609375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6851458549499512})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5157632827758789})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.43607234954833984})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.44756364822387695})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42647290229797363})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [53316, 55488, 40874, 41962, 42294, 16210, 22159, 55480, 22559, 56188], 'labels': [5, 3, 6, 9, 0, 5, 0, 7, 6, 2], 'scores': [0.4500095248222351, 0.41302138566970825, 0.3508930802345276, 0.4652913808822632, 0.4906767010688782, 0.47487324476242065, 0.4236604571342468, 0.38051342964172363, 0.35309135913848877, 0.3890764117240906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8425365686416626})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6178075671195984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6360903978347778})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6977912187576294})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7706423997879028})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.554195703125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7244076132774353})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5507765412330627})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5284746289253235})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5296766757965088})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [30642, 37158, 22091, 43083, 22229, 4360, 32734, 2765, 54646, 55390], 'labels': [3, -1, 6, 0, 2, 6, 6, 0, 6, 6], 'scores': [0.36761003732681274, 0.36428797245025635, 0.5736143589019775, 0.4906312823295593, 0.478454053401947, 0.6328497529029846, 0.6488214731216431, 0.5450993776321411, 0.5386776924133301, 0.40368014574050903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9440017342567444})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6729520559310913})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.600054919719696})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6828014850616455})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.727723240852356})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6712599992752075})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.555835009765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.744297981262207})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5284913182258606})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4972589612007141})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45382195711135864})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4514051675796509})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [5619, 11404, 8297, 3178, 45925, 25744, 24156, 14655, 20967, 39503], 'labels': [-1, -1, 7, -1, 9, -1, -1, 3, 2, 0], 'scores': [0.37970542907714844, 0.36241602897644043, 0.5039102435112, 0.35374003648757935, 0.6767730712890625, 0.2551053762435913, 0.3202436566352844, 0.5643329620361328, 0.40710628032684326, 0.5045003890991211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7817550897598267})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5472441911697388})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5748541355133057})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5735642910003662})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6254816055297852})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.54216435546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.726097583770752})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5999647974967957})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5285178422927856})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5133336782455444})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [30704, 29440, 30844, 27344, 5846, 9392, 53979, 42078, 43454, 19396], 'labels': [9, 7, 8, 9, 6, -1, 8, 4, 5, 5], 'scores': [0.46937060356140137, 0.40655362606048584, 0.44182848930358887, 0.3660101890563965, 0.30696672201156616, 0.18730199337005615, 0.5549134016036987, 0.5016153454780579, 0.262237012386322, 0.5346808433532715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8939181566238403})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5901654958724976})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5843251347541809})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5701386332511902})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6001101732254028})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6270277500152588})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6076785326004028})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9282, 'crossentropy': 0.5349208984375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7230745553970337})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5053261518478394})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43930584192276})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4371219277381897})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39914876222610474})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3920319676399231})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [45987, 49715, 38410, 42153, 2152, 27573, 13081, 34718, 52163, 18473], 'labels': [5, 8, 3, 0, -1, -1, 0, 2, 6, 4], 'scores': [0.4654198884963989, 0.4843766689300537, 0.4849625825881958, 0.5280650854110718, 0.3209770917892456, 0.28114771842956543, 0.43136394023895264, 0.32512617111206055, 0.3714545965194702, 0.5187963247299194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.02547025680542})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5816912651062012})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5872963666915894})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.605199933052063})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.616642951965332})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.583245849609375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7455153465270996})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.628309965133667})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5502728223800659})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5200255513191223})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [57213, 52216, 2213, 1473, 40413, 58026, 20641, 43126, 24587, 19362], 'labels': [-1, 7, 7, 4, 2, 2, 9, 3, 8, 8], 'scores': [0.26725542545318604, 0.49664896726608276, 0.5742124319076538, 0.36831486225128174, 0.4230996370315552, 0.40125006437301636, 0.5202569365501404, 0.5049774646759033, 0.49005889892578125, 0.4780157804489136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9141829013824463})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5240004062652588})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5431544780731201})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5329340100288391})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.561415433883667})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.5273546875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7607191801071167})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5611361861228943})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5057246088981628})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5150012969970703})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [22095, 47601, 8821, 8586, 20170, 18256, 39015, 49890, 8780, 33130], 'labels': [1, 1, 3, 9, 9, 1, -1, 5, 8, 9], 'scores': [0.4768415689468384, 0.5374664068222046, 0.32572925090789795, 0.49235057830810547, 0.5106972455978394, 0.4036639928817749, 0.3550223112106323, 0.4846349358558655, 0.37958329916000366, 0.5089938044548035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8675152063369751})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5044406652450562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5191187262535095})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45531630516052246})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5234742164611816})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5304684638977051})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5493669509887695})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.41710576171875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7149465084075928})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.505143404006958})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3873043656349182})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4014012813568115})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3588278293609619})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3549429178237915})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [49987, 22531, 42958, 30401, 47234, 35116, 17296, 21295, 4063, 5616], 'labels': [0, 4, -1, 8, 1, -1, 9, 8, 8, 3], 'scores': [0.344135582447052, 0.3887975811958313, 0.4037367105484009, 0.30849090218544006, 0.38599610328674316, 0.2344188690185547, 0.3957010507583618, 0.5183862745761871, 0.42038142681121826, 0.33662718534469604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8611268997192383})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47430163621902466})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46326643228530884})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5213934779167175})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4681698679924011})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4717083275318146})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9447, 'crossentropy': 0.42348701171875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7897158861160278})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4710323214530945})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.440247118473053})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.40801942348480225})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3814764618873596})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [47016, 44172, 16836, 57837, 55667, 31313, 29248, 50889, 50054, 59202], 'labels': [5, 8, 7, 5, 5, -1, 5, -1, 8, 3], 'scores': [0.4273808002471924, 0.4259450435638428, 0.473572313785553, 0.4736540913581848, 0.4859194755554199, 0.35225069522857666, 0.2986931800842285, 0.3534198999404907, 0.5911648273468018, 0.35711541771888733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9678217172622681})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5644252896308899})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.473530650138855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.51241135597229})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48774299025535583})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5225925445556641})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.453853076171875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6893818974494934})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4992472529411316})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46288323402404785})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4262016713619232})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40250062942504883})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [57550, 29621, 8639, 44095, 1164, 9567, 33193, 6990, 51071, 4688], 'labels': [-1, -1, 5, 2, -1, 8, 8, -1, 4, -1], 'scores': [0.45491230487823486, 0.3877859115600586, 0.41785264015197754, 0.5044645071029663, 0.2943382263183594, 0.3648824691772461, 0.3438379168510437, 0.43285155296325684, 0.41619014739990234, 0.429394006729126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.066918134689331})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48048168420791626})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5133921504020691})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47619497776031494})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5270606279373169})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5120199918746948})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.590994119644165})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.44451015625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7556430101394653})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5321623682975769})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39102405309677124})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36739715933799744})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35436686873435974})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3611809015274048})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [36755, 29004, 47292, 43950, 18486, 17786, 19924, 1682, 34713, 32738], 'labels': [3, -1, 9, 9, -1, -1, 0, 0, -1, 7], 'scores': [0.41035085916519165, 0.34105122089385986, 0.4671849012374878, 0.3675631284713745, 0.4676007032394409, 0.2735256552696228, 0.4845110774040222, 0.5510721802711487, 0.26533329486846924, 0.4758898615837097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8210684061050415})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48383328318595886})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49023616313934326})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4224932789802551})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4929223358631134})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4745957851409912})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5243805646896362})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.3922937255859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.716731071472168})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4898417890071869})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40576648712158203})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36992523074150085})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40289682149887085})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.378639280796051})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [30566, 23083, 4705, 10256, 6945, 5847, 37688, 11667, 20304, 59361], 'labels': [-1, -1, -1, 2, -1, -1, 9, 2, 7, 8], 'scores': [0.3101040720939636, 0.3050679564476013, 0.36669230461120605, 0.5213210582733154, 0.28541743755340576, 0.3239908218383789, 0.5612162351608276, 0.4265154004096985, 0.3109395503997803, 0.4524967074394226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9190672039985657})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4962090253829956})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4611254930496216})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49827632308006287})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4918437898159027})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4750637412071228})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.441795947265625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7411412000656128})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5339637994766235})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4831768572330475})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4143558740615845})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4186173677444458})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [33983, 10108, 9870, 45066, 3094, 59492, 31108, 32045, 59196, 22788], 'labels': [-1, -1, -1, -1, 8, 5, 3, 4, 5, -1], 'scores': [0.31976091861724854, 0.2326650619506836, 0.3616352081298828, 0.3536949157714844, 0.4655550718307495, 0.30769550800323486, 0.4203854203224182, 0.3979622721672058, 0.411459743976593, 0.35696637630462646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0947976112365723})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5657243728637695})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4701553285121918})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46787136793136597})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46001917123794556})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4586738348007202})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4582585394382477})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45350146293640137})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4564908742904663})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5349345207214355})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5255270004272461})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.3989958740234375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7289667725563049})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4864211976528168})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4094066023826599})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3664807677268982})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3523648679256439})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3621045649051666})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3406680226325989})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3308592736721039})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.319568395614624})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3123851418495178})
store['active_learning_steps'][24]['eval_training']['best_epoch']=10
store['active_learning_steps'][24]['acquisition']={'indices': [23086, 57985, 28757, 36363, 35145, 41307, 52889, 2034, 49563, 44289], 'labels': [8, 4, -1, 6, -1, 4, -1, 4, 8, -1], 'scores': [0.47508758306503296, 0.4983679950237274, 0.4965958595275879, 0.5228389501571655, 0.6153801679611206, 0.47195011377334595, 0.6598992347717285, 0.5534259080886841, 0.7355585098266602, 0.3888934850692749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8897984027862549})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5092087984085083})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4948764145374298})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43464577198028564})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4181623160839081})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43163377046585083})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4492380619049072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4943463206291199})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.38632568359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8460757732391357})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5059187412261963})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42812830209732056})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37529945373535156})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36203816533088684})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35935837030410767})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34877991676330566})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [28575, 43649, 7636, 24905, 3916, 52526, 36919, 9340, 30923, 54446], 'labels': [-1, -1, 8, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.4193074703216553, 0.33102136850357056, 0.3856803774833679, 0.23360908031463623, 0.3584263324737549, 0.3021479845046997, 0.308790385723114, 0.4507763385772705, 0.3538944721221924, 0.4682779312133789]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0347900390625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5736109018325806})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46060216426849365})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5185348987579346})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4993129372596741})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4789806008338928})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9446, 'crossentropy': 0.3920377685546875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8854671716690063})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5067621469497681})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4865732491016388})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42091619968414307})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3950798511505127})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [54380, 11708, 55856, 4043, 37062, 16047, 52683, 45800, 41009, 53570], 'labels': [-1, 3, 9, -1, 9, 2, -1, 9, -1, 3], 'scores': [0.27602851390838623, 0.5405669808387756, 0.3435856103897095, 0.3863043785095215, 0.3322107791900635, 0.32730531692504883, 0.2530437707901001, 0.4387866258621216, 0.3027604818344116, 0.44982850551605225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0083669424057007})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5781999826431274})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4693036675453186})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4418264627456665})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4270046353340149})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44749513268470764})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4519845247268677})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4474935531616211})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.373371044921875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8863407373428345})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5191127061843872})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4103381931781769})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39021754264831543})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3964771032333374})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3605145812034607})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.333434522151947})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [51324, 14762, 44461, 25306, 27680, 21426, 20939, 18126, 6834, 17739], 'labels': [8, -1, -1, 6, 2, 6, 3, 8, -1, 5], 'scores': [0.5291705131530762, 0.39417028427124023, 0.39873993396759033, 0.46989667415618896, 0.5110583603382111, 0.5318542718887329, 0.53483647108078, 0.4109530448913574, 0.3347427248954773, 0.5036939382553101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0494122505187988})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6022346615791321})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47380250692367554})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43936479091644287})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49175941944122314})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44562485814094543})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44722747802734375})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.40284091796875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7667890787124634})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5041742324829102})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4399482011795044})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4020426273345947})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38465166091918945})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.379942923784256})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [54919, 24915, 21880, 12051, 1648, 33505, 4165, 37124, 49497, 42121], 'labels': [8, -1, 2, -1, 2, 2, 2, 3, 0, 5], 'scores': [0.2991674542427063, 0.40212130546569824, 0.6421681642532349, 0.3485180139541626, 0.4732153117656708, 0.42056554555892944, 0.5988512635231018, 0.24437665939331055, 0.5576423406600952, 0.4604828357696533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.18333101272583})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5229572057723999})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42659667134284973})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41304346919059753})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43033039569854736})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4727133512496948})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43282678723335266})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.3776781982421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8027268648147583})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48507994413375854})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.429057776927948})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3971409797668457})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42258787155151367})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3503437638282776})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [10570, 38142, 53019, 43112, 50426, 37383, 4634, 45256, 27986, 470], 'labels': [2, 8, 2, -1, 7, 3, 8, 5, 7, 1], 'scores': [0.36642634868621826, 0.4385344982147217, 0.4459173083305359, 0.36034393310546875, 0.48813122510910034, 0.6116253733634949, 0.4605521559715271, 0.3744378685951233, 0.2327612042427063, 0.6071115732192993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9406954646110535})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5112656354904175})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4183260202407837})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38036930561065674})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3808627724647522})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3971092700958252})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4003749489784241})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3587798095703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8338741660118103})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5289814472198486})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42254799604415894})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3912789523601532})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3822150230407715})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37118804454803467})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [3762, 13878, 27632, 14715, 54316, 20726, 45520, 16022, 57221, 35882], 'labels': [8, 4, 7, 4, -1, 4, 8, 8, -1, 2], 'scores': [0.4374557137489319, 0.45604389905929565, 0.476057231426239, 0.5517286062240601, 0.3617926239967346, 0.2768126428127289, 0.3674502372741699, 0.48900288343429565, 0.3618776202201843, 0.45480769872665405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.034571886062622})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5056837797164917})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42446449398994446})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3676528334617615})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36140328645706177})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3826459050178528})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39037322998046875})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37814855575561523})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9569, 'crossentropy': 0.340260205078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8929917812347412})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4746054410934448})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4593488574028015})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3895198702812195})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3813885450363159})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3758509159088135})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34944817423820496})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [3430, 12828, 2907, 48570, 11808, 15269, 40807, 45380, 23970, 42920], 'labels': [-1, -1, 1, -1, -1, -1, 7, -1, 1, -1], 'scores': [0.2983516454696655, 0.3990633487701416, 0.3956869840621948, 0.4063602685928345, 0.45867979526519775, 0.28940510749816895, 0.34482376277446747, 0.37823379039764404, 0.3970338702201843, 0.27035510540008545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9649044871330261})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5217127799987793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41290992498397827})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3783879280090332})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3792950510978699})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4088113307952881})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4086926579475403})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9553, 'crossentropy': 0.335508447265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8137989044189453})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4888499081134796})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40740686655044556})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38037800788879395})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3552715480327606})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32816070318222046})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [59983, 22139, 53675, 30806, 32926, 23423, 10938, 17684, 57221, 27576], 'labels': [2, 2, 5, 8, 8, 9, 0, 2, -1, 5], 'scores': [0.4267622232437134, 0.48089146614074707, 0.29691970348358154, 0.4048117399215698, 0.4467810392379761, 0.3954964876174927, 0.44688212871551514, 0.3216503858566284, 0.30653703212738037, 0.496002197265625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0710290670394897})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5145125389099121})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.45283886790275574})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40475767850875854})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3431573510169983})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35093092918395996})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3897533416748047})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3681761622428894})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.3231033203125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8994643092155457})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4916340112686157})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4322611093521118})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3801012635231018})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3359307050704956})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3624208867549896})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3158450722694397})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [3209, 24887, 15836, 31687, 44738, 38922, 46389, 2434, 36072, 54480], 'labels': [-1, 5, 2, -1, -1, 4, 6, -1, 2, -1], 'scores': [0.28882670402526855, 0.47315800189971924, 0.4648500680923462, 0.16175353527069092, 0.38220930099487305, 0.37537240982055664, 0.3283478915691376, 0.2825040817260742, 0.6138086318969727, 0.2634153366088867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9691798686981201})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5263826847076416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33463093638420105})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3580177426338196})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33153966069221497})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35964345932006836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33780160546302795})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3352492153644562})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.3144324462890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9131214618682861})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5965677499771118})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42395859956741333})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3960552513599396})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3450426459312439})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.350309282541275})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30589598417282104})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [52927, 42172, 17079, 13241, 49660, 23956, 47002, 22119, 2803, 29633], 'labels': [1, -1, 6, -1, 8, 4, -1, 8, 3, 7], 'scores': [0.48480087518692017, 0.4353998899459839, 0.5305364727973938, 0.4279667139053345, 0.45128577947616577, 0.6272263526916504, 0.32442647218704224, 0.31363797187805176, 0.40311485528945923, 0.3873196244239807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1181920766830444})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5046887397766113})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4026497006416321})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34636977314949036})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3614044189453125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3433986306190491})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3720840811729431})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37305787205696106})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34711623191833496})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3022744140625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8330944776535034})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4963739514350891})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36661073565483093})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34933775663375854})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3476664125919342})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31336167454719543})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3190637230873108})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29689788818359375})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [8339, 52127, 21495, 49543, 13404, 6900, 55368, 44350, 52346, 50184], 'labels': [5, 9, 9, 8, 5, 1, 8, -1, 4, 3], 'scores': [0.3322567343711853, 0.49931395053863525, 0.37677669525146484, 0.40047550201416016, 0.3910598158836365, 0.4276478886604309, 0.4891427159309387, 0.2519322633743286, 0.3062029778957367, 0.3282856345176697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9799502491950989})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5183186531066895})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.380792498588562})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37777912616729736})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39217913150787354})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33892905712127686})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3691139221191406})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3780696392059326})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39842936396598816})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.308884326171875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8902992010116577})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5318936705589294})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36516904830932617})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37127965688705444})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34444475173950195})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3367998003959656})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30279743671417236})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3182724118232727})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [28723, 52169, 25748, 18247, 23717, 32668, 14749, 5065, 13524, 40046], 'labels': [-1, 2, 7, 0, -1, 9, 0, -1, 3, 7], 'scores': [0.2775670886039734, 0.5978100299835205, 0.3831202983856201, 0.4076036214828491, 0.41376376152038574, 0.5157406330108643, 0.5864329934120178, 0.23241186141967773, 0.4269391894340515, 0.47951608896255493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0507336854934692})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49530625343322754})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3589223027229309})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3614673614501953})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3307371139526367})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30074939131736755})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3386467695236206})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3316056728363037})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34758642315864563})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2711591796875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7873897552490234})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47057241201400757})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3575844168663025})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3145495057106018})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32790637016296387})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28493595123291016})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27949583530426025})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2892642021179199})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [6462, 43648, 26898, 29018, 4432, 1402, 42086, 1323, 25666, 48280], 'labels': [-1, -1, 7, -1, -1, -1, 9, -1, -1, -1], 'scores': [0.3831430673599243, 0.40705984830856323, 0.33255535364151, 0.3586781620979309, 0.5220075845718384, 0.43372631072998047, 0.2684481143951416, 0.4284524917602539, 0.47368359565734863, 0.5458524227142334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1450841426849365})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5087273120880127})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40168559551239014})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3211490213871002})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33110129833221436})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34348779916763306})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3350670337677002})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.2843181640625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8024373054504395})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4818319082260132})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38646024465560913})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32748571038246155})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3231152892112732})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3043287992477417})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [50371, 21148, 33364, 21896, 29286, 59151, 16722, 24830, 12005, 28757], 'labels': [7, 7, 2, 8, 9, 3, 1, 7, -1, 3], 'scores': [0.36495041847229004, 0.5019578337669373, 0.43264085054397583, 0.4137207269668579, 0.39919352531433105, 0.3795589208602905, 0.5306222438812256, 0.40583351254463196, 0.31652581691741943, 0.26767170429229736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8897476196289062})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5177397727966309})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3735208511352539})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31491610407829285})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29895541071891785})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33551937341690063})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30040788650512695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33124685287475586})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.271089990234375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.846262514591217})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5151486396789551})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3835127353668213})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3575964868068695})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30759096145629883})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2867877185344696})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2971455454826355})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [28420, 13677, 49206, 32784, 33598, 33121, 1231, 54028, 24669, 39680], 'labels': [1, 8, -1, 8, -1, -1, -1, -1, 4, -1], 'scores': [0.4801349639892578, 0.5363270044326782, 0.40860676765441895, 0.4130364656448364, 0.4079322814941406, 0.3235074281692505, 0.2637132406234741, 0.4545590877532959, 0.3754730224609375, 0.2690238952636719]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.135499119758606})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5534615516662598})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3802664279937744})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32257506251335144})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3118342161178589})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3051421344280243})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37988168001174927})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3459978699684143})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.326898992061615})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.2936824462890625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8269472122192383})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5103235840797424})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3319580852985382})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33229586482048035})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3157117962837219})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29016992449760437})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3012561798095703})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.282792866230011})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [35960, 8274, 31850, 17094, 47720, 39899, 10557, 45535, 8469, 19440], 'labels': [-1, -1, 7, -1, -1, 2, -1, -1, -1, -1], 'scores': [0.46853697299957275, 0.3099428415298462, 0.564654678106308, 0.44031310081481934, 0.3945200443267822, 0.5694940686225891, 0.3013143539428711, 0.3770245313644409, 0.4455915689468384, 0.37636828422546387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.120219349861145})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49476176500320435})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3844282031059265})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3528572916984558})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32540541887283325})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3266203999519348})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.330178439617157})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3622441291809082})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.301739892578125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.848243236541748})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4716053605079651})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3729628920555115})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36017006635665894})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31631600856781006})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2941664159297943})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3402542769908905})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [36122, 34520, 12665, 27653, 49700, 25823, 54298, 24684, 54880, 14909], 'labels': [-1, 6, 0, 6, 4, 0, -1, 9, 5, 6], 'scores': [0.2402637004852295, 0.5390869081020355, 0.40370315313339233, 0.41519689559936523, 0.26412519812583923, 0.33191579580307007, 0.2723270654678345, 0.3380240797996521, 0.3994920253753662, 0.460879921913147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0606908798217773})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5582542419433594})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.359133243560791})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34301501512527466})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30555102229118347})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35397613048553467})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3025889992713928})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33113810420036316})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3008792996406555})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34194689989089966})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30017954111099243})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29873543977737427})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4128683805465698})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31625503301620483})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31104767322540283})
store['active_learning_steps'][42]['training']['best_epoch']=12
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2953898681640625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8928110003471375})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.498163104057312})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3977389931678772})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30309659242630005})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3007013201713562})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27126723527908325})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2715281546115875})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2587917447090149})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23909778892993927})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23839561641216278})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2377529740333557})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23239287734031677})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23147697746753693})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23204050958156586})
store['active_learning_steps'][42]['eval_training']['best_epoch']=13
store['active_learning_steps'][42]['acquisition']={'indices': [971, 53873, 53910, 7349, 59783, 36628, 22866, 17200, 25964, 1220], 'labels': [-1, 4, 2, -1, 1, 0, 5, 0, -1, -1], 'scores': [0.41179919242858887, 0.690402626991272, 0.5321093797683716, 0.526427686214447, 0.6698981523513794, 0.5611478984355927, 0.7253010272979736, 0.6163630485534668, 0.4849073886871338, 0.3905898332595825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0755903720855713})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5196300745010376})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38816148042678833})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34941810369491577})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29289332032203674})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30376994609832764})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31649142503738403})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3155866861343384})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.2889280517578125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8076861500740051})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47652533650398254})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4061538875102997})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35722485184669495})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30849140882492065})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29698431491851807})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2961725890636444})
store['active_learning_steps'][43]['eval_training']['best_epoch']=7
store['active_learning_steps'][43]['acquisition']={'indices': [46069, 41942, 2622, 37402, 53817, 23095, 42348, 40717, 30944, 1728], 'labels': [0, -1, 5, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4691762924194336, 0.4252270460128784, 0.48904556035995483, 0.39717525243759155, 0.47029542922973633, 0.3562507629394531, 0.35230767726898193, 0.41383981704711914, 0.45877909660339355, 0.4827108383178711]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9805030822753906})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.48419511318206787})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3597255051136017})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32350221276283264})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3082849681377411})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2996949851512909})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33311155438423157})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2912220060825348})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2960536479949951})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3078235685825348})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3394017219543457})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.259972802734375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8712918758392334})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4298306107521057})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35240742564201355})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3321528434753418})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32372957468032837})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.294594943523407})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2682952582836151})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26793208718299866})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2643367648124695})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24874377250671387})
store['active_learning_steps'][44]['eval_training']['best_epoch']=10
store['active_learning_steps'][44]['acquisition']={'indices': [32141, 11057, 12744, 8670, 48481, 58000, 57097, 16107, 52914, 40589], 'labels': [-1, -1, 6, 2, -1, -1, -1, -1, 5, -1], 'scores': [0.31099963188171387, 0.41946864128112793, 0.4319058656692505, 0.6256120800971985, 0.33111751079559326, 0.3552849292755127, 0.3649296760559082, 0.3165804147720337, 0.5134101510047913, 0.4115869402885437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0687485933303833})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4393380284309387})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3639177083969116})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3409085273742676})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27036118507385254})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30982479453086853})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.287672758102417})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2782939374446869})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.2551867919921875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.827345609664917})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46588873863220215})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36457955837249756})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38825634121894836})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31623226404190063})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3072158396244049})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.290802001953125})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [36133, 21923, 27238, 18833, 10260, 4954, 59589, 55238, 2152, 21576], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3880126476287842, 0.5547749996185303, 0.42336952686309814, 0.38847869634628296, 0.5283242464065552, 0.43957364559173584, 0.3491077423095703, 0.31475234031677246, 0.4077824354171753, 0.3184218406677246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0084238052368164})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5560867786407471})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3675505518913269})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3088844418525696})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3560745120048523})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3061075210571289})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3348977863788605})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3123466372489929})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3216472864151001})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.2745420654296875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8428349494934082})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4737072288990021})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3805084228515625})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3146410882472992})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3146549463272095})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3161184787750244})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29719239473342896})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2954460680484772})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [27613, 12306, 36721, 42830, 1238, 20113, 9057, 43677, 47471, 44865], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 7], 'scores': [0.30778658390045166, 0.4860575795173645, 0.33931636810302734, 0.4067342281341553, 0.4777323603630066, 0.3486407995223999, 0.4553998112678528, 0.24043619632720947, 0.3728140592575073, 0.5836480259895325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9814542531967163})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4790658950805664})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3632899522781372})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32886356115341187})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3061635196208954})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3053058981895447})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28815460205078125})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2791582942008972})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30660152435302734})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.311690092086792})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2996768355369568})
store['active_learning_steps'][47]['training']['best_epoch']=8
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.26671826171875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8103955984115601})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4549593925476074})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34472745656967163})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3090020418167114})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26037806272506714})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27607885003089905})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27452293038368225})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23785194754600525})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2338377833366394})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23699694871902466})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [20433, 682, 47796, 32276, 12862, 31329, 14629, 45596, 43448, 57428], 'labels': [-1, -1, -1, 3, -1, -1, 0, -1, -1, -1], 'scores': [0.49575817584991455, 0.4395461678504944, 0.45264703035354614, 0.5654218196868896, 0.441707968711853, 0.4142911434173584, 0.41192370653152466, 0.4475972056388855, 0.30107760429382324, 0.5294183492660522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0442485809326172})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5240825414657593})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3937031328678131})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34996747970581055})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.297110915184021})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3637251853942871})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31458503007888794})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31156909465789795})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.2666635986328125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7544206380844116})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5032464265823364})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3698640465736389})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34432607889175415})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30512815713882446})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29393142461776733})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2940096855163574})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [28224, 22607, 14333, 44091, 14410, 38673, 38182, 26294, 31272, 47451], 'labels': [-1, 4, 3, 4, -1, -1, -1, 8, -1, -1], 'scores': [0.4173234701156616, 0.5532960295677185, 0.40206050872802734, 0.42999058961868286, 0.37503373622894287, 0.3271104097366333, 0.3451775312423706, 0.31061244010925293, 0.31996452808380127, 0.3009836673736572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.024757981300354})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5152075886726379})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44955965876579285})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.349093496799469})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30551815032958984})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36785078048706055})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3406471014022827})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34498611092567444})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.306618505859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8402901291847229})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47705742716789246})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34914523363113403})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33126044273376465})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33906418085098267})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3525359034538269})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3039480745792389})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [45408, 57718, 47599, 8932, 54099, 29343, 39480, 46941, 48638, 57311], 'labels': [3, 7, 0, 0, 7, 5, 9, 5, 0, 5], 'scores': [0.42958879470825195, 0.46260499954223633, 0.440915048122406, 0.5615231990814209, 0.35128313302993774, 0.3101775646209717, 0.3959317207336426, 0.36144500970840454, 0.47077733278274536, 0.45315295457839966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1789942979812622})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5444865226745605})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41243165731430054})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3340888023376465})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3092353343963623})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29624229669570923})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3127630352973938})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31212833523750305})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29581472277641296})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3453649580478668})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32861125469207764})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33996444940567017})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.3000653564453125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8483832478523254})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46914514899253845})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3691987991333008})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31077924370765686})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31434959173202515})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2921714782714844})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24529963731765747})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25433945655822754})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26651519536972046})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2593330442905426})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [12239, 4185, 52218, 52392, 15666, 39841, 2111, 37287, 24633, 32408], 'labels': [-1, 2, -1, 1, -1, -1, -1, -1, 2, -1], 'scores': [0.5187913179397583, 0.6160340309143066, 0.34476184844970703, 0.5400201678276062, 0.346288800239563, 0.4912331700325012, 0.3706028461456299, 0.3796924352645874, 0.5368879437446594, 0.20942604541778564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0839624404907227})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5696007013320923})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41846710443496704})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34838393330574036})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29271918535232544})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3116772174835205})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29842716455459595})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29603931307792664})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.28077734375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.960600733757019})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5105754137039185})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41575169563293457})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33247068524360657})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3545982241630554})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32111936807632446})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31489789485931396})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [52140, 11155, 56603, 12704, 7938, 43069, 18104, 6405, 33198, 49041], 'labels': [4, -1, -1, -1, -1, -1, -1, -1, 8, 2], 'scores': [0.41985756158828735, 0.3607158660888672, 0.23929357528686523, 0.39833319187164307, 0.35721296072006226, 0.30028557777404785, 0.36103272438049316, 0.32532286643981934, 0.441364586353302, 0.35603463649749756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0935254096984863})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.556326150894165})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3410739302635193})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3340788185596466})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.303766667842865})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3388183116912842})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2907814681529999})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3046955168247223})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3120088577270508})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3018327057361603})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2649526611328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8082334995269775})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45586541295051575})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3317035138607025})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32061314582824707})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.282535195350647})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28155651688575745})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27739185094833374})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2476138174533844})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26088374853134155})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [4761, 5536, 20233, 21858, 18324, 50441, 2372, 1826, 48546, 25705], 'labels': [-1, -1, -1, -1, 0, -1, -1, -1, -1, -1], 'scores': [0.3092820644378662, 0.4350321888923645, 0.5557349920272827, 0.23357582092285156, 0.6692991852760315, 0.3775146007537842, 0.46599435806274414, 0.3854749798774719, 0.28828173875808716, 0.4876999855041504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2281464338302612})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5799828767776489})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3977445363998413})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3475337028503418})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29792124032974243})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3258562982082367})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3101906180381775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.299741268157959})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.2702924072265625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8616179823875427})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47773659229278564})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.40547919273376465})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3456001877784729})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3377217650413513})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34318602085113525})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2918792963027954})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [3810, 32702, 56198, 12306, 21558, 25508, 55896, 58700, 12689, 54878], 'labels': [3, 5, -1, -1, 5, -1, 7, -1, -1, 4], 'scores': [0.3712306022644043, 0.44232165813446045, 0.40700340270996094, 0.35366398096084595, 0.5400481820106506, 0.45034366846084595, 0.34378981590270996, 0.3079078197479248, 0.5477151870727539, 0.40528249740600586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0891954898834229})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5326187610626221})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3719836473464966})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34379154443740845})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31563812494277954})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29461508989334106})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30214905738830566})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3078365623950958})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3173825442790985})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.268885595703125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8799977898597717})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5093624591827393})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38228243589401245})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3357897698879242})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.307037353515625})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29024577140808105})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28951629996299744})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27995532751083374})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [26405, 43059, 7294, 21296, 33362, 31345, 32535, 38791, 47291, 42427], 'labels': [9, -1, 6, -1, 7, 3, -1, 8, 1, -1], 'scores': [0.452287495136261, 0.32010936737060547, 0.48735523223876953, 0.39404916763305664, 0.45844849944114685, 0.38073408603668213, 0.3030507564544678, 0.34325721859931946, 0.4287008047103882, 0.33410370349884033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1229283809661865})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6035150289535522})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4250375032424927})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37086576223373413})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3414730429649353})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3190481662750244})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34527158737182617})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30395016074180603})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3606053590774536})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31499534845352173})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3462200164794922})
store['active_learning_steps'][55]['training']['best_epoch']=8
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.2844022705078125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8625462055206299})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5163438320159912})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36224621534347534})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3236922025680542})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2820127010345459})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26091253757476807})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26667261123657227})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2839779555797577})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25183212757110596})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2595762014389038})
store['active_learning_steps'][55]['eval_training']['best_epoch']=9
store['active_learning_steps'][55]['acquisition']={'indices': [41299, 13099, 48880, 23136, 49280, 43702, 1674, 54097, 30900, 10412], 'labels': [3, 3, 4, 0, 0, 3, 9, 7, 5, 5], 'scores': [0.51300448179245, 0.46395862102508545, 0.7349538207054138, 0.42600297927856445, 0.4703707695007324, 0.5543559789657593, 0.5444349050521851, 0.3920983672142029, 0.546371728181839, 0.6626411080360413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1490747928619385})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5398087501525879})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3568609952926636})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34337425231933594})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36246949434280396})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28836292028427124})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2864864766597748})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30580615997314453})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3292959928512573})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3131003975868225})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2751867919921875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7999292612075806})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4596928358078003})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40218544006347656})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3241790533065796})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31296032667160034})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2764495611190796})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26718008518218994})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2506367266178131})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25416862964630127})
store['active_learning_steps'][56]['eval_training']['best_epoch']=8
store['active_learning_steps'][56]['acquisition']={'indices': [17890, 38287, 59406, 41378, 46650, 54593, 12704, 11492, 20169, 1135], 'labels': [5, 5, -1, -1, -1, -1, -1, 5, 4, 5], 'scores': [0.41671866178512573, 0.4562971591949463, 0.3749798536300659, 0.44205886125564575, 0.3437911868095398, 0.42072808742523193, 0.4141499996185303, 0.45774126052856445, 0.5475097298622131, 0.5526708960533142]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0677728652954102})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.508331835269928})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44290339946746826})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31689321994781494})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2904854118824005})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3119812607765198})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26745253801345825})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2869102954864502})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3142850995063782})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30078911781311035})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2634806640625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0178420543670654})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5324596166610718})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4115334153175354})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36124032735824585})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31681013107299805})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2828151285648346})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.291083425283432})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3170108199119568})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2944034934043884})
store['active_learning_steps'][57]['eval_training']['best_epoch']=6
store['active_learning_steps'][57]['acquisition']={'indices': [35201, 36647, 7862, 32657, 30154, 35445, 10119, 5164, 35697, 51974], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4502396583557129, 0.5350821018218994, 0.4475870132446289, 0.4242526888847351, 0.32508355379104614, 0.4118812084197998, 0.3315783739089966, 0.3345956802368164, 0.4033489227294922, 0.24935448169708252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.917411208152771})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4345155656337738})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35487914085388184})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32931286096572876})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32805556058883667})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32155072689056396})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29754015803337097})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3146423101425171})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28107723593711853})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2970064878463745})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3027174174785614})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31543511152267456})
store['active_learning_steps'][58]['training']['best_epoch']=9
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2774427001953125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9315890073776245})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5060561895370483})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3731148838996887})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34096062183380127})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30982622504234314})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27868008613586426})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29798632860183716})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2646028995513916})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2720903754234314})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24563297629356384})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2702663540840149})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [13396, 44745, 15972, 7800, 55531, 54049, 35022, 30111, 48379, 52306], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, 8], 'scores': [0.1790783405303955, 0.4945562481880188, 0.42887234687805176, 0.4914734363555908, 0.5118520855903625, 0.6181616187095642, 0.3906409740447998, 0.44722622632980347, 0.5768865942955017, 0.6607181429862976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1098353862762451})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.593585729598999})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41737839579582214})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3637350797653198})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3021537661552429})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3163040280342102})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34564200043678284})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3158610463142395})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.2878415771484375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9033772945404053})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49428224563598633})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40238237380981445})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37769973278045654})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34228643774986267})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32592135667800903})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34541356563568115})
store['active_learning_steps'][59]['eval_training']['best_epoch']=6
store['active_learning_steps'][59]['acquisition']={'indices': [26932, 15303, 12663, 54106, 24630, 52897, 13259, 32190, 30359, 52694], 'labels': [-1, -1, 8, 7, 5, -1, 1, 7, 7, 2], 'scores': [0.1949237585067749, 0.23486745357513428, 0.4106428027153015, 0.316378653049469, 0.32304954528808594, 0.19692480564117432, 0.40285158157348633, 0.39668309688568115, 0.3317597508430481, 0.46752703189849854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.094278335571289})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.577716052532196})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40177732706069946})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32128992676734924})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32058441638946533})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3097579777240753})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3045041561126709})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3072904348373413})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3364415466785431})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.335280179977417})
store['active_learning_steps'][60]['training']['best_epoch']=7
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2742507568359375}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9316419959068298})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4802643060684204})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3596484065055847})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35244035720825195})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30258893966674805})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2978670597076416})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28909799456596375})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2776643931865692})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2720627188682556})
store['active_learning_steps'][60]['eval_training']['best_epoch']=9
store['active_learning_steps'][60]['acquisition']={'indices': [18398, 9661, 54296, 26241, 42059, 1886, 7868, 21526, 49655, 22130], 'labels': [4, 8, 3, -1, 9, -1, -1, -1, -1, 5], 'scores': [0.6469646692276001, 0.4210042357444763, 0.4690961241722107, 0.471407949924469, 0.4714900255203247, 0.5415588617324829, 0.3251192569732666, 0.5364007353782654, 0.385111927986145, 0.4459553360939026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.124365210533142})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5421375036239624})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38928866386413574})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3389415144920349})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30978935956954956})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35234999656677246})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36101704835891724})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32490068674087524})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2856465087890625}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9566386938095093})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5312370657920837})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47733819484710693})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3711487352848053})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3429349362850189})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3506225347518921})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31775012612342834})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [37098, 19136, 35401, 47860, 32097, 19495, 16795, 16453, 49354, 7870], 'labels': [-1, -1, 3, -1, -1, 3, 7, 3, 0, -1], 'scores': [0.47826337814331055, 0.5163156986236572, 0.5757325291633606, 0.4144887924194336, 0.28832149505615234, 0.44412535429000854, 0.2885301113128662, 0.4631270170211792, 0.43774664402008057, 0.33371663093566895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.101963996887207})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5255937576293945})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3508739471435547})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3319249451160431})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3047655522823334})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34388789534568787})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3271586298942566})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3056097626686096})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.28185166015625}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9178214073181152})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49615341424942017})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4287504553794861})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.363874226808548})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3292062282562256})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33364367485046387})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3355751931667328})
store['active_learning_steps'][62]['eval_training']['best_epoch']=5
store['active_learning_steps'][62]['acquisition']={'indices': [58213, 34942, 51863, 17502, 18754, 16627, 54933, 45491, 45602, 6390], 'labels': [9, 9, 9, -1, -1, 2, 6, 5, 5, -1], 'scores': [0.3090639114379883, 0.4271048903465271, 0.474481463432312, 0.34046119451522827, 0.27897584438323975, 0.5498858094215393, 0.44412004947662354, 0.3628529906272888, 0.3780185580253601, 0.22208726406097412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.2622568607330322})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6342684030532837})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4736870527267456})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35534530878067017})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34831753373146057})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3615221679210663})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30034393072128296})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31585973501205444})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3278966248035431})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3112563490867615})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.269595166015625}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8950985074043274})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5811428427696228})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39028245210647583})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3574223220348358})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3148524761199951})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3173248767852783})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30997705459594727})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31559211015701294})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2995525896549225})
store['active_learning_steps'][63]['eval_training']['best_epoch']=9
store['active_learning_steps'][63]['acquisition']={'indices': [25480, 19081, 30248, 12605, 54167, 1788, 21010, 24667, 1792, 4153], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2], 'scores': [0.49557673931121826, 0.48889732360839844, 0.33926498889923096, 0.3478766679763794, 0.5928900241851807, 0.44042718410491943, 0.4536951780319214, 0.5215467810630798, 0.4424736499786377, 0.7183341383934021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1076102256774902})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47302499413490295})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41283661127090454})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3345015048980713})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30792123079299927})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30186203122138977})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30658039450645447})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29884448647499084})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2854558229446411})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28981220722198486})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3024194836616516})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2942906618118286})
store['active_learning_steps'][64]['training']['best_epoch']=9
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.24865419921875}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9566959142684937})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5254798531532288})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3626190423965454})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33764493465423584})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3081039488315582})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26952776312828064})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2662457227706909})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2632364332675934})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26493674516677856})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2534768283367157})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24021798372268677})
store['active_learning_steps'][64]['eval_training']['best_epoch']=11
store['active_learning_steps'][64]['acquisition']={'indices': [21642, 33767, 27024, 52834, 19168, 54697, 17792, 25907, 12655, 47728], 'labels': [4, -1, 8, 2, 1, -1, 9, 2, 9, -1], 'scores': [0.5552746057510376, 0.33905744552612305, 0.3850775957107544, 0.620633065700531, 0.34447264671325684, 0.293664813041687, 0.4850718677043915, 0.5161687731742859, 0.311212420463562, 0.3025473356246948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0748212337493896})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5234251618385315})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3805699646472931})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3390524685382843})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29288768768310547})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.299713134765625})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2814418375492096})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28290683031082153})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2699991464614868})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2898271679878235})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2970038056373596})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29853323101997375})
store['active_learning_steps'][65]['training']['best_epoch']=9
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.253297900390625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9897140860557556})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5198822021484375})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3804399371147156})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3543708324432373})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34587937593460083})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2914315462112427})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.286582887172699})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24031361937522888})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26145458221435547})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24315977096557617})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2554553747177124})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [41508, 16838, 46018, 27802, 5089, 34133, 4754, 36505, 39768, 38912], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.21879160404205322, 0.30925846099853516, 0.41786813735961914, 0.412847638130188, 0.43276476860046387, 0.4775732159614563, 0.4995185136795044, 0.35520052909851074, 0.3674124479293823, 0.4085122346878052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.094573736190796})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5629773139953613})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39403674006462097})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3623157739639282})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29845771193504333})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3119240403175354})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30721479654312134})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2872549593448639})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2962792217731476})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30945807695388794})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3207707703113556})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2456320556640625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.951532781124115})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5374594926834106})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3964969515800476})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3732338547706604})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3021489977836609})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27247288823127747})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2984597980976105})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2966032326221466})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24787777662277222})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2994728684425354})
store['active_learning_steps'][66]['eval_training']['best_epoch']=9
store['active_learning_steps'][66]['acquisition']={'indices': [40827, 38920, 36985, 53148, 18598, 56649, 10382, 19662, 28102, 8417], 'labels': [-1, -1, -1, 6, 9, -1, -1, -1, 0, 6], 'scores': [0.30232107639312744, 0.3542729616165161, 0.5447255373001099, 0.39515751600265503, 0.3974835276603699, 0.35559654235839844, 0.3663962483406067, 0.3307664394378662, 0.6389882564544678, 0.2908935844898224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0455632209777832})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5902135968208313})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38716405630111694})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3471906781196594})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33357882499694824})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3245545029640198})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32348504662513733})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28919297456741333})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3249604403972626})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29362791776657104})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30203646421432495})
store['active_learning_steps'][67]['training']['best_epoch']=8
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.257220654296875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9758203029632568})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.535152792930603})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3813803791999817})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.304117351770401})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3104970157146454})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2659246027469635})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24070164561271667})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2508748173713684})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2420971691608429})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26050320267677307})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [13243, 13195, 1899, 21901, 2369, 50995, 12271, 28902, 5575, 6574], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5259802341461182, 0.6844884753227234, 0.2832922339439392, 0.5568217635154724, 0.5570032596588135, 0.45998042821884155, 0.3778432607650757, 0.5522580146789551, 0.6017488241195679, 0.3330821394920349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1439990997314453})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.606878399848938})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3812897801399231})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3412342369556427})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28798845410346985})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35405051708221436})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33313247561454773})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.321239173412323})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.2750258544921875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8801442384719849})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5594607591629028})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3796110153198242})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3905189037322998})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34575170278549194})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3176461458206177})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31029272079467773})
store['active_learning_steps'][68]['eval_training']['best_epoch']=7
store['active_learning_steps'][68]['acquisition']={'indices': [57714, 24, 13855, 37624, 25701, 36028, 52562, 31014, 1925, 2845], 'labels': [1, 1, -1, -1, -1, -1, -1, 8, -1, 8], 'scores': [0.4984191060066223, 0.43096649646759033, 0.19316381216049194, 0.35272181034088135, 0.4798187017440796, 0.3331339359283447, 0.5232877135276794, 0.47694170475006104, 0.37998151779174805, 0.4446260929107666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2062195539474487})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5424318313598633})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.39714115858078003})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3031003475189209})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2990131378173828})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3087380528450012})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28910231590270996})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2939135432243347})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3246108889579773})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31683892011642456})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2632580810546875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9393414258956909})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4647524356842041})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4373127222061157})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3831362724304199})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31445229053497314})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2785867154598236})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28994083404541016})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2601465582847595})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26627057790756226})
store['active_learning_steps'][69]['eval_training']['best_epoch']=8
store['active_learning_steps'][69]['acquisition']={'indices': [35406, 1486, 39395, 9384, 4446, 22722, 40208, 15728, 41879, 35145], 'labels': [5, -1, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.510926365852356, 0.4556899070739746, 0.29214227199554443, 0.5635003447532654, 0.39878225326538086, 0.3311845064163208, 0.368808388710022, 0.3896297216415405, 0.3668476343154907, 0.3915363550186157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2477552890777588})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6033186316490173})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44852209091186523})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.366820752620697})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3048444390296936})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3050372898578644})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33490777015686035})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3263416290283203})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.277789111328125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0375957489013672})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.527942419052124})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3940792977809906})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35482555627822876})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35569947957992554})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3354019522666931})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3323969542980194})
store['active_learning_steps'][70]['eval_training']['best_epoch']=7
store['active_learning_steps'][70]['acquisition']={'indices': [36892, 33897, 8617, 14004, 47378, 54869, 29501, 45127, 42843, 24061], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3903278112411499, 0.20748603343963623, 0.3875981569290161, 0.263210654258728, 0.36837196350097656, 0.3074929714202881, 0.43002915382385254, 0.358070969581604, 0.33170223236083984, 0.35596799850463867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1816883087158203})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.555905282497406})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35826581716537476})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3322402834892273})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3051738142967224})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2840358316898346})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2792859971523285})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3293777108192444})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27951931953430176})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3242540955543518})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.24720341796875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9087302684783936})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.456465482711792})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4185553789138794})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36380907893180847})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30826419591903687})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2823456823825836})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2847018241882324})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26880237460136414})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25182634592056274})
store['active_learning_steps'][71]['eval_training']['best_epoch']=9
store['active_learning_steps'][71]['acquisition']={'indices': [43189, 17592, 52205, 33426, 36464, 39877, 46899, 37247, 27838, 3223], 'labels': [-1, 4, -1, 4, -1, 7, 3, 9, 3, -1], 'scores': [0.29856717586517334, 0.43180903792381287, 0.36514854431152344, 0.5691546499729156, 0.1994481086730957, 0.5337920188903809, 0.40784287452697754, 0.4470348358154297, 0.32931727170944214, 0.33582353591918945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0229249000549316})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6054574251174927})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40168967843055725})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32312867045402527})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33089590072631836})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2826906442642212})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2527497410774231})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2847457230091095})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2768869698047638})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2578586935997009})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2532055419921875}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8791868090629578})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48293614387512207})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37255099415779114})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32080352306365967})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3039204180240631})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2746875286102295})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26433950662612915})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2666674554347992})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.286094605922699})
store['active_learning_steps'][72]['eval_training']['best_epoch']=7
store['active_learning_steps'][72]['acquisition']={'indices': [53313, 34847, 39300, 2837, 58543, 22806, 1220, 11721, 3115, 41378], 'labels': [-1, 0, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5015897154808044, 0.5287327170372009, 0.4544931650161743, 0.4640614986419678, 0.27159225940704346, 0.3573042154312134, 0.4705672264099121, 0.4785352945327759, 0.48616909980773926, 0.470874547958374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.287591576576233})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6300296783447266})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5158127546310425})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33180007338523865})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33493363857269287})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2897135615348816})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3059917688369751})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2632649838924408})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3150531053543091})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2671130895614624})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3126068115234375})
store['active_learning_steps'][73]['training']['best_epoch']=8
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.26750517578125}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9628510475158691})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5434116125106812})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4215124249458313})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35327446460723877})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2787379026412964})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2889402508735657})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27567288279533386})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2931322455406189})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2868433892726898})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2599591314792633})
store['active_learning_steps'][73]['eval_training']['best_epoch']=10
store['active_learning_steps'][73]['acquisition']={'indices': [18910, 49242, 52785, 35075, 4010, 13016, 55699, 33176, 31084, 1313], 'labels': [7, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5700321197509766, 0.41008496284484863, 0.4981391429901123, 0.43818068504333496, 0.32069605588912964, 0.4735037088394165, 0.3151106834411621, 0.4535750150680542, 0.42923927307128906, 0.5570275783538818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1827768087387085})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.580769956111908})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3694450259208679})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3269837498664856})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3274005353450775})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3083858788013458})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28361356258392334})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25505390763282776})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31671690940856934})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30924609303474426})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28740769624710083})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.232173046875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9484176635742188})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5549368262290955})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3837287425994873})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3166060447692871})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2975653409957886})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2752845287322998})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2812988758087158})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26364991068840027})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2471444010734558})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2705342769622803})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [25706, 10840, 3122, 17415, 49971, 2297, 48315, 45295, 41289, 4536], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3223426342010498, 0.2884511351585388, 0.4167715311050415, 0.2683964967727661, 0.3745887279510498, 0.4387440085411072, 0.39167261123657227, 0.2753901481628418, 0.617822527885437, 0.44189292192459106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.138559103012085})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5606571435928345})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3787359595298767})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31467536091804504})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28806743025779724})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2812894582748413})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24705618619918823})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24866139888763428})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26774919033050537})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2970757484436035})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.249153125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8442275524139404})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47658681869506836})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4191535711288452})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32834160327911377})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3173573613166809})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2969765067100525})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2864598333835602})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2654035687446594})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2802807092666626})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [49039, 890, 9588, 56364, 63, 59115, 35246, 34524, 38958, 54230], 'labels': [-1, -1, 7, 4, -1, -1, 8, 8, -1, 5], 'scores': [0.5049367547035217, 0.4089397192001343, 0.5797585248947144, 0.6141822338104248, 0.43398118019104004, 0.4553263187408447, 0.5529167652130127, 0.6745502948760986, 0.5221409797668457, 0.388296902179718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.230029582977295})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6066526174545288})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3800196051597595})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3259070813655853})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2965180277824402})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3054555058479309})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26543205976486206})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24588528275489807})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28669270873069763})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2348761111497879})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2784450054168701})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30497872829437256})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.281278133392334})
store['active_learning_steps'][76]['training']['best_epoch']=10
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.23061279296875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9203946590423584})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48235851526260376})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40349844098091125})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33822327852249146})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2900397777557373})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27816665172576904})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29243069887161255})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28671473264694214})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2544129192829132})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2624690532684326})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2438807636499405})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2389780580997467})
store['active_learning_steps'][76]['eval_training']['best_epoch']=12
store['active_learning_steps'][76]['acquisition']={'indices': [2426, 34752, 23091, 59542, 35281, 29491, 40893, 13646, 57128, 10486], 'labels': [1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.5253347754478455, 0.4822123050689697, 0.5117257833480835, 0.5592482089996338, 0.4725378751754761, 0.3259918689727783, 0.4966632127761841, 0.5144245624542236, 0.33544838428497314, 0.3894255757331848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2382107973098755})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5563434362411499})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3785420060157776})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3118566572666168})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2844666540622711})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28129732608795166})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2568196952342987})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2381749153137207})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24470043182373047})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2673223614692688})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2590082287788391})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.228135595703125}
